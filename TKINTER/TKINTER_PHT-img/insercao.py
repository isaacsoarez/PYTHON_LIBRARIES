from tkinter import *

# manipulação de arquivos e execução de comandos do sistema
import os

# Direcionado de pasta
pastaApp = os.path.dirname(__file__)

app = Tk()
app.title("INSERÇÃO DE IMAGEM")

app.geometry("500x300")

# Encaminhador de arquivo através da pasta 
imgLogo = PhotoImage(file=os.path.join(pastaApp, "simpsons.gif"))

l_logo = Label(app, image=imgLogo)
l_logo.place(x=800, y=300)
# (x=750, y=10)

# Encerramento do comando geral
app.mainloop()
