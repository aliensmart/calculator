import tkinter

window = tkinter.Tk()
window.title("labels")

tkinter.Label(window, bg = "#9b59b6", text = "middle", fg = "white").pack()

tkinter.Label(window, text = "full X", bg = "#e74c3c", fg = "white").pack(fill = "x")

tkinter.Label(window, text = "full X", bg = "#e74c3c", fg = "white").pack(fill = "y", side = "right")


window.mainloop()