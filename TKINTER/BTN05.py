import tkinter as tk

gui = tk.Tk()
gui.geometry("500x200")
gui.title("Page")
gui['bg'] = '#ccc'

def on_select():
    opcao_selecionado = radion_var.get()
    print(f'Você selecionou:{opcao_selecionado}')

radion_var = tk.StringVar()

radion_botao1 = tk.Radiobutton(gui, text="option 1", variable=radion_var, value="option 1", command=on_select)
radion_botao2 = tk.Radiobutton(gui, text="option 2", variable=radion_var, value="option 2", command=on_select)
radion_botao3 = tk.Radiobutton(gui, text="option 3", variable=radion_var, value="option 3", command=on_select)

radion_botao1.pack()
radion_botao2.pack()
radion_botao3.pack()


gui.mainloop()