import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Toplevel, Text, Button
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline
import torch, threading, os

root = tk.Tk()  # Creates a blank window
root.title("Tkinter AI GUI")
root.resizable(False, False)
root.geometry("700x650")  # enlarged from GUI3 

# Color theme
root.configure(bg="light blue")
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='blue', foreground='white')
style.map('TButton', background=[('active', 'red')])

# Helpers
def run_in_thread(fn, *a, **k):
    threading.Thread(target=fn, args=a, kwargs=k, daemon=True).start()

def log(msg: str):
    outputBox.insert("end", msg + "\n"); outputBox.see("end")

def fit_image_for_preview(img: Image.Image, box_w: int, box_h: int) -> Image.Image:
    im = img.copy()
    im.thumbnail((box_w, box_h), Image.LANCZOS)
    return im

def _best_device():
    if torch.backends.mps.is_available(): return "mps"
    if torch.cuda.is_available(): return "cuda"
    return "cpu"

def set_model_info(name: str, category: str, desc: str):
    modelNameLbl.config(text=f"• Model Name: {name}")
    modelCatLbl.config(text=f"• Category (Text, Vision, Audio): {category}")
    modelDescLbl.config(text=f"• Short Description: {desc}")

def set_busy(is_busy: bool):
    state = "disabled" if is_busy else "normal"
    run1Btn.config(state=state)
    run2Btn.config(state=state)
    loadModelbut.config(state=state)

# Model state
_t2i_pipe = None
_t2i_loading = False
_last_gen_path = None
current_file_path = None

# Text-to-Image loader
def load_text2image():
    global _t2i_pipe, _t2i_loading
    if _t2i_pipe is not None: return _t2i_pipe
    if _t2i_loading: return None
    _t2i_loading = True
    try:
        device = _best_device()
        dtype = torch.float16 if device == "cuda" else torch.float32
        log(f"Loading Text-to-Image model on {device} (dtype={dtype})…")

        pipe = StableDiffusionPipeline.from_pretrained("stabilityai/sd-turbo", torch_dtype=dtype)

        if hasattr(pipe, "enable_attention_slicing"): pipe.enable_attention_slicing()
        if hasattr(pipe, "enable_vae_slicing"):       pipe.enable_vae_slicing()
        if hasattr(pipe, "enable_vae_tiling"):        pipe.enable_vae_tiling()
        try: pipe.set_progress_bar_config(disable=True)
        except Exception: pass

        if device != "cpu":
            pipe = pipe.to(device)

        try:
            with torch.inference_mode():
                _ = pipe("warmup", num_inference_steps=1, guidance_scale=0.0, height=256, width=256).images[0]
        except Exception:
            pass

        _t2i_pipe = pipe
        set_model_info(
            name="stabilityai/sd-turbo",
            category="Computer Vision (Text → Image)",
            desc="Very fast distilled Stable Diffusion runs well with 1–2 steps."
        )
        log("Model loaded.")
        return _t2i_pipe
    finally:
        _t2i_loading = False

# Text-to-Image generation
def generate_image():
    def _work():
        global _last_gen_path
        set_busy(True)
        try:
            pipe = load_text2image()
            if pipe is None:
                log("Model is still loading…"); return
            prompt = inputText.get("1.0", "end").strip() or "a cute robot reading a book, 3d render, soft light"
            log("Generating…")

            generator = torch.Generator(device=_best_device()).manual_seed(42)
            with torch.inference_mode():
                image = pipe(
                    prompt,
                    num_inference_steps=2,
                    guidance_scale=0.0,
                    height=384, width=384,
                    generator=generator
                ).images[0]

            out_path = "t2i_output.png"
            image.save(out_path); _last_gen_path = out_path

            prev = fit_image_for_preview(image, 240, 170)
            tk_img = ImageTk.PhotoImage(prev)
            root.after(0, lambda: (img_label.config(image=tk_img), setattr(img_label, "image", tk_img)))
            root.after(0, lambda: log(f"Generated image saved to: {out_path}"))
        finally:
            root.after(0, lambda: set_busy(False))

    run_in_thread(_work)

# Model Selection
Label(root, text="Model Selection:").place(x=10, y=8)
options = ["Text-to-Image"]
selectedItem = tk.StringVar(value="Text-to-Image")
combobox = ttk.Combobox(root, textvariable=selectedItem, values=options, state="readonly", width=22)
combobox.place(x=130, y=5)

def load_model_clicked():
    run_in_thread(load_text2image)

loadModelbut = tk.Button(root, text="Load Model", command=load_model_clicked, fg="white", bg="blue")
loadModelbut.place(x=360, y=5, width=110, height=24)

# User Input Section
left_box = ttk.Labelframe(root, text="User Input Section")
left_box.place(x=10, y=60, width=390, height=220)

var = IntVar(value=1)
ttk.Radiobutton(left_box, text="Text",  variable=var, value=1).place(x=10, y=8)
ttk.Radiobutton(left_box, text="Image", variable=var, value=2).place(x=90, y=8)

def browseFile():
    global current_file_path
    path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All files", "*.*")]
    )
    if path:
        current_file_path = path
        log(f"Selected file: {path}")
        try:
            img = Image.open(path)
            prev = fit_image_for_preview(img, 240, 170)
            tk_img = ImageTk.PhotoImage(prev)
            img_label.config(image=tk_img); img_label.image = tk_img
        except Exception:
            pass

ttk.Button(left_box, text="Browse", command=browseFile).place(x=300, y=5)

inputText = tk.Text(left_box)
inputText.place(x=10, y=36, width=370, height=120)
inputText.insert("1.0", "a cute robot reading a book")

run1Btn  = ttk.Button(left_box, text="Run Model 1", command=generate_image)
run2Btn  = ttk.Button(left_box, text="Run Model 2", command=generate_image)
clearBtn = ttk.Button(left_box, text="Clear", command=lambda: outputBox.delete("1.0", "end"))
run1Btn.place(x=10,  y=165, width=120)
run2Btn.place(x=140, y=165, width=120)
clearBtn.place(x=270, y=165, width=110)

# Model Output Section
right_box = ttk.Labelframe(root, text="Model Output Section")
right_box.place(x=420, y=60, width=260, height=340)

ttk.Label(right_box, text="Output Display:").place(x=10, y=6)
outputBox = ScrolledText(right_box, wrap="word")
outputBox.place(x=10, y=26, width=240, height=120)

img_label = tk.Label(right_box, bd=1, relief="sunken", cursor="hand2")
img_label.place(x=10, y=156, width=240, height=170)

def show_full_image(_=None):
    path = _last_gen_path or current_file_path
    if not path or not os.path.exists(path): return
    img = Image.open(path)
    img.thumbnail((1000, 800), Image.LANCZOS)
    top = Toplevel(root); top.title("Full Preview")
    tkimg = ImageTk.PhotoImage(img)
    lbl = Label(top, image=tkimg); lbl.image = tkimg
    lbl.pack()

img_label.bind("<Button-1>", show_full_image)

# Model Information & Explanation
info_box = ttk.Labelframe(root, text="Model Information & Explanation")
info_box.place(x=10, y=430, width=680, height=180)

for i in (0, 1):
    info_box.columnconfigure(i, weight=1)

ttk.Label(info_box, text="Selected Model Info:").grid(row=0, column=0, sticky="w", padx=8, pady=(6, 2))
modelNameLbl = ttk.Label(info_box, text="• Model Name: (not loaded)", wraplength=320, justify="left")
modelCatLbl  = ttk.Label(info_box, text="• Category (Text, Vision, Audio): (choose)", wraplength=320, justify="left")
modelDescLbl = ttk.Label(info_box, text="• Short Description: —", wraplength=320, justify="left")
modelNameLbl.grid(row=1, column=0, sticky="w", padx=12)
modelCatLbl.grid(row=2, column=0, sticky="w", padx=12)
modelDescLbl.grid(row=3, column=0, sticky="w", padx=12)

ttk.Label(info_box, text="OOP Concepts Explanation:").grid(row=0, column=1, sticky="w", padx=8, pady=(6, 2))
oopLbl = ttk.Label(
    info_box,
    text=("• Where Multiple Inheritance is used\n"
          "• Why Encapsulation was applied\n"
          "• How Polymorphism & Method Overriding are shown\n"
          "• Where Multiple Decorators are applied"),
    justify="left"
)
oopLbl.grid(row=1, column=1, rowspan=3, sticky="nw", padx=12)

# Menu
menu = Menu(root); root.config(menu=menu)
fileMenu = Menu(menu, tearoff=0)
fileMenu.add_command(label="Open File", command=browseFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.destroy)
menu.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menu, tearoff=0)
def show_about():
    top = Toplevel(root); top.title("About")
    msg = "HIT137 – Tkinter + Hugging Face (sd-turbo) demo."
    Label(top, text=msg, padx=12, pady=12).pack()
    Button(top, text="OK", command=top.destroy).pack(pady=6)
helpMenu.add_command(label="About", command=show_about)
menu.add_cascade(label="Help", menu=helpMenu)

root.mainloop()
