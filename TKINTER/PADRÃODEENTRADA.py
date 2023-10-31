import tkinter as tk

window = tk.Tk()
window.title('como definir o texto padrão')
window.state('zoomed')

rotulo = tk.Label(window, text="coloque sua cor favorita")
rotulo.pack()

#criar um widget de entrada com valor padrao
default_text = "black"
entry = tk.Entry(window)
entry.insert(0, default_text)
entry.pack()

window.mainloop()