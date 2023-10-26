import tkinter as tk
from tkinter import font


window = tk.Tk()
window.geometry("500x500")
window.title("Redimensionando Janela")
window["bg"]= '#fff'

label_font = font.Font(size=60)
label = tk.Label(window, wraplength=300, font=label_font, text="")
label.pack()



def janela_redimensao(event):

    largura=event.width
    altura=event.height
    print(f'Janela redimensionada! {largura}x{altura}')


window.bind("<Configure>", janela_redimensao)

window.mainloop()