from tkinter import *
import tkinter.filedialog
import customtkinter as ctk

root = Tk("Text Editor")
root.title("Text Editor")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry("600x400")
root.minsize(600, 400)

text = Text(root)
text.grid(row=0, column=0, sticky="nsew")

ctk.set_default_color_theme("dark-blue")

def save():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = ctk.CTkButton(root, text='Save File', command=save)
button.grid(padx=10, pady=10)

def change_font(font_family, font_size):
    global text
    text.config(font=(font_family, font_size))
    font["text"] = f"({font_family})"

def font_courier():
    global text
    text.config(font="Courier")
    font["text"] = "Courier"

def font_helvetica():
    global text
    text.config(font="Helvetica")
    font["text"] = "Helvetica"

font = Menubutton(root, text="Change Font")
font.grid(sticky="s")
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

font_family = StringVar()
font_size = IntVar()

helvetica = IntVar()
courier = IntVar()
font.menu.add_radiobutton(label="Courier", variable=font_family, value="Courier", command=font_courier)
font.menu.add_radiobutton(label="Helvetica", variable=font_family, value="Helvetica", command=font_helvetica)

font_size_frame = Frame(root)
font_size_frame.grid(sticky="s")

font_size_label = Label(font_size_frame, text="Change Font Size:")
font_size_label.pack(side="left")

def change_font_size(size):
    change_font(font_family.get(), size)

small_button = ctk.CTkButton(font_size_frame, text="Small", command=lambda: change_font_size(12))
small_button.pack(side="left", padx=5, pady=5)

medium_button = ctk.CTkButton(font_size_frame, text="Medium", command=lambda: change_font_size(18))
medium_button.pack(side="left", padx=5, pady=5)

large_button = ctk.CTkButton(font_size_frame, text="Large", command=lambda: change_font_size(24))
large_button.pack(side="left", padx=5, pady=5)

root.mainloop()
