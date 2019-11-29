from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Alerte Box")

#creating a simple alert box
tkinter.messagebox.showinfo("Alerte Message", "This is just a alert message!")

#creating a question to get the response from the user
response = tkinter.messagebox.askquestion("simple Question", "Do you love Python?")

#if user click 'yes' then it return 1 else it return 0
if response == 1:
    Label(window, text = "You do love python").pack()
else:
    Label(window, text = "You don't like python??")


window.mainloop()