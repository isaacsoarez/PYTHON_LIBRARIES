#funções da lib são atribuídas 
import tkinter as tk 
#import qrcode #pip install qrcode
#from PIL import Image, ImageDraw #pip install pillow
#from tkinter import messagebox
from tkinter import*

#_____________________________________________________#

#atribui a variavel a WINDOW a uma função
window = tk.Tk()

#atribui um nome a janela criada
window.title("My first window")

window.resizable(False, True)

#troca cor da janela
window.configure(bg="red", borderwidth="5")
window.geometry("300x1000")


#gui=Graphic User Interface
gui = Tk(className="workout with TkInter")

#configurar tamanha da janela
gui.geometry("1000x2000")
gui.configure(bg="red")


#executa a variavel window(JANELA)
window.mainloop()

#_____________________________________________________#
