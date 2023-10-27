from tkinter import *

tkWindow = Tk()
tkWindow.geometry("400x150")
tkWindow.title("PythonExamples.org - Tkinter Example")

def toggletext():
    if button["text"] == "Submit":
        button["text"] = "Submitted"
    else:
        button["text"] = "Submit"

button = Button(tkWindow, text='Submit', command=toggletext)
button.pack()

tkWindow.mainloop()
