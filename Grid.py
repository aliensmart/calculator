import tkinter

window = tkinter.Tk()

window.title("Grid")


tkinter.Label(window, text = "Your Username").grid(row = 0)
tkinter.Entry(window).grid(row = 0, column = 1)
tkinter.Label(window, text = "Your password").grid(row = 1, column = 0)
tkinter.Entry(window).grid(row = 1, column = 1)

tkinter.Checkbutton(window, text = "Keep me Loggin").grid(columnspan = 2)

tkinter.Button(window, text = "Login", bg = "#d35400", fg = "white").grid(columnspan = 3)

window.mainloop()