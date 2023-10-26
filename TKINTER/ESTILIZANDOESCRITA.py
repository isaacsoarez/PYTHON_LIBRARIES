from tkinter import*

tkWindow = Tk()
tkWindow.geometry("400x250")
tkWindow.title("Trocando as config's do botão")

def mudarTexto():
    button["text"] = "Enviado"

button = Button(tkWindow, text="Enviar", command=mudarTexto)
button.pack()

tkWindow.state('zoomed')

tkWindow.mainloop()