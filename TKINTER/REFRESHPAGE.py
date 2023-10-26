import tkinter as tk
from tkinter import font

window = tk.Tk()
window.geometry("500x500")
window.title("Redimensionando Janela")
window["bg"]= '#fff'

label_font = font.Font(size=60)
label = tk.Label(window, wraplength=300, font=label_font, text="")
label.pack()

def atualizar_window():

    window.update()
    window.update_idletasks()
    print(f'Janela atualizada com sucesso!')

label= tk.Label(window, text="clicar no botão de refresh")

label.pack()

botao = tk.Button(window, text="Atualizar", command=atualizar_window)

botao.pack()

window.mainloop()