import tkinter as tk

from tkinter import filedialog, messagebox

import subprocess

import os

class SadTalkerApp:

def init (self, root):

self.root root

self.root.title("SadTalker Video Generator")

self.root.geometry("500x400")

self.image path = None

self.ppt_path=None

self audio path None
tk.Label(root, text="Upload Inputs", font=("Helvetica", 16)).pack(pady-10)

tk.Button(root, text="Upload Image", command=self.upload_image).pack(pady-5)

tk.Button(root, text="Upload PPT", command=self.upload_ppt).pack(pady=5)

tk.Button(root, text="Upload Audio (Optional)",

command=self.upload_audio).pack(pady-5)

tk.Button(root, text="Generate Video", command=self.run_pipeline, bg="green". fg="white").pack(pady-20)

self.status label tk.Label(root, text="", fg="blue")

self.status label.pack(pady=10)

def upload_image(self):

self.image path filedialog.askopenfilename(filetypes=[("Image Files", "* jpg .png.jpeg")])

self.status_label.config(text=f"Selected image: {os.path.basename(self.image path)}")
def upload_ppt(self):

self.ppt_path= filedialog.askopenfilename(filetypes=[("PowerPoint Files", "*.pptx")])

self.status_label.config(text-f"Selected PPT: ({os.path.basename(self.ppt_path)}")

def upload_audio(self):

self.audio_path filedialog askopenfilename(filetypes=[("Audio Files", "* wav *.mp3")])

self status label.config(text=f"Selected audio"):

(os.path.basename(self.audio_path))")

def run pipeline(self):

if not self.image path or not self.ppt_path:

messagebox.showerror("Error", "Please upload both Image and PPT")

return

X

emd["python", "main.py", "-image", self.image_path, "--ppt", self.ppt_path]

if self.audio path:

cmd += ["--audio", self.audio_path]

self.status_label.config(text="Processing... Please wait 8")
try:

subprocess.run(cmd, check-True)

self.status_label.config(text="✔ Video Generated! Check 'outputs' folder.")

except subprocess.CalledProcessError:

self.status label.config(text="X Error during generation.")



messagebox.showerror("Error", "Something went wrong while generating video.")

if name="main_":

roottk.Tk()

app SadTalkerApp(root)

root.mainloop()