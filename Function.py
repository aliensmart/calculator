from tkinter import *

window = Tk()

window.title("function")


def say_hi():
    
    Label(window, text = "Hi").pack()


Button(window, text = "Click me", command = say_hi).pack()

window.mainloop()
