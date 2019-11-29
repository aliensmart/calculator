from tkinter import *

window = Tk()

window.title("function")


def say_hi():
    
    Label(window, text = "Hi").pack()

def left_click(event):
    Label(window, text = "Left Click").pack()

def right_click(event):
    Label(window, text = "Right CLick").pack()

def middle_click(mousemove):
    Label(window, text = "Middle Click").pack()

Button(window, text = "Click me", command = say_hi).pack()

window.bind("<Button-1>", left_click)
window.bind("mousemove",middle_click)
window.bind("<Button-3>", right_click)

window.mainloop()
