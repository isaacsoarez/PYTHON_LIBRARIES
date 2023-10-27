from tkinter import*
import tkinter.font as font

gui = Tk(className='Python example - Button')
gui.geometry("500x200")

myFont = font.Font(size=30)
button = Button(gui, text='My button', bg='#0052cc', fg='#fff')

button['font'] = myFont

button.pack()
gui.mainloop()