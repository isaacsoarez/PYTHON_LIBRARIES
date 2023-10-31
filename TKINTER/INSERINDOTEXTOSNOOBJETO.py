import tkinter as tk

janela = tk.Tk()
janela.title('Inserindo textos no label')
janela.geometry('300x300')

label = tk.Label(janela, text='coloque uma informação')
label.pack()

def inserir_valor_entry():
    entry.insert(0, "hello world")

def limpar_campos():
    entry.delete(0, tk.END)

entry = tk.Entry(janela)
entry.pack()

botao = tk.Button(janela, text='inserir', command=inserir_valor_entry)
botao.pack()

botao = tk.Button(janela, text="limpar", command=limpar_campos)
botao.pack()


janela.mainloop()