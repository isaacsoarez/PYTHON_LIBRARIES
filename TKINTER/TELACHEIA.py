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

label= tk.Label(window, text="Pressione [ESC] para fechar a janela")

label.pack()

window.bind("<Escape>", lambda e, w=window: w.destroy())


def botao_clique():
    window.destroy()

botao = tk.Button(window, text="Fechar Janela", command=botao_clique)
botao.pack()

#maximizar window
window.state("zoomed")

window.mainloop()
