import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("300x1000")
window.title("Page")
window['bg'] = '#ccc'

window["padx"] = 100
window["pady"] = 50

label_font = font.Font(size=60)
label = tk.Label(window, wraplength=300, font=label_font, text="EU SOU O HENRIQUE")
label.pack()

# Carregue a imagem usando Pillow
imagem = Image.open("hendev.jpg")

# Aumente o tamanho da imagem
nova_largura = 400  # Substitua pelo valor desejado
nova_altura = 400  # Substitua pelo valor desejado
nova_imagem = imagem.resize((nova_largura, nova_altura))

# Converta a nova imagem para ImageTk
imagem_ampliada = ImageTk.PhotoImage(nova_imagem)

label_imagem = tk.Label(window, image=imagem_ampliada)
label_imagem.pack()

window.mainloop()
