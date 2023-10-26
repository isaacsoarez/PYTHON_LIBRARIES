import tkinter as tk 
from tkinter import font

window = tk.Tk()
window.geometry("300x1000")
window.title("Page")
window['bg'] = '#ccc'

window["padx"] = 100

window["pady"] = 50


label_font = font.Font(size=60)
label = tk.Label(window, wraplength=300, font=label_font , text="Henrique treina glúteo isolado")

label.pack()

window.mainloop()