from tkinter import*

gui = Tk(className="Criando Botões")
gui.geometry("300x300")

#atribui função
botao = Button(gui, text="Boão Inicial", width=30, height=4, bg="#ccc", activeforeground="#aaffaa")
botao.pack()

gui.state('zoomed')

gui.mainloop()
