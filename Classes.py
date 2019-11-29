from tkinter import *

class Rand:
    
    def __init__(self, root):
        self.root = root
        self.text_btn = Button(root, text = "say Hi", command = self.say_hi).pack()

        self.close = Button(root, text = "Close", command = root.quit).pack()

    
    def say_hi(self):
        Label(self.root, text = "Hi").pack()

    


window = Tk()
window.title("Class")

rand = Rand(window)

window.mainloop()