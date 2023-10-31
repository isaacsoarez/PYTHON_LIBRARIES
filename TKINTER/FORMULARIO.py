from tkinter import *
from functools import partial

#Nosso exemplo sera pra ler o nome do usuario



def imprimirDetalhes(usuarioDigitado):
    usuarioTexto = usuarioDigitado.get()
    print('usuario digitado:', usuarioTexto)
    return

tkTela = Tk()
tkTela.geometry("400x200")
tkTela.title('Exemplos de entrada e de saída')


usuarioLabel = Label(tkTela, text='Digite o nome do usuário')


usuarioDigitado = Entry(tkTela)

imrpeimirDetalhesMostrado = partial(imprimirDetalhes, usuarioDigitado)

botaoEnviar = Button(tkTela, text="Enviar", command=imrpeimirDetalhesMostrado)


usuarioLabel.grid(row=0, column=0)
usuarioDigitado.grid(row=0, column=1)
botaoEnviar.grid(row=1, column=1)

tkTela.mainloop()
