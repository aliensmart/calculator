import tkinter

window = tkinter.Tk()
window.title("Image")

#Taking image from the directory and storing images
ima = tkinter.PhotoImage(file = "images/download.png")
#displaying the picture using a Label by passing the picture variables to image parameter
tkinter.Label(window, image = ima).pack()

window.mainloop()