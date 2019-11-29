from tkinter import *

Window = Tk()
Window.title("Shapes")

#Cretaing the width area with width and height 500px

canvas = Canvas(Window, width = 500, height = 500)

canvas.pack()

#creates_line is used to create a line. Parameters:0 (starting x-point, starting y-point, ending x-point, ending y-point)
line1 = canvas.create_line(25, 25, 120, 100, fill = "red")
line2 = canvas.create_line(120, 100, 125, 25)


#creating rectangle is used to create rectangle. Parameters -(starting xpoint, starting ypoint, width, heigh, fill)
#starting point the coordinates of top-left point of rectangle

rect = canvas.create_rectangle(500, 25, 175,75, fill = "green")


Window.mainloop()