import tkinter as tk
from tkinter import messagebox

tela = tk.Tk()
tela.title('capturar senhas digitadas')
tela.geometry('450x300')

def pegar_password():
    senha = entry.get()
    print('a senha é:', senha)
    messagebox.showwarning('A senha é:', senha)


entry = tk.Entry(tela, show="*")
entry.pack()

botao = tk.Button(tela, text="Exibir senha:", command=pegar_password)
botao.pack()


tela.mainloop()