import tkinter

window = tkinter.Tk()

window.title("Calculator")

#creating two frame, top and bottom

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")


#now, create some widget

btn1 = tkinter.Button(top_frame, text= "button1", bg = "#3498db", fg = "white").pack(side= "right")
btn2 = tkinter.Button(top_frame, text="Button2", bg = "#3498db", fg = "white").pack(side= "left")

btn3 = tkinter.Button(bottom_frame, text = "button3", bg = "#16a085", fg = "white").pack(side = "bottom")
btn4 = tkinter.Button(bottom_frame, text = "button4", bg = "#16a085", fg = "white").pack(side = "bottom")


window.mainloop()


# # creating 2 frames TOP and BOTTOM
# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# # now, create some widgets in the top_frame and bottom_frame
# btn1 = tkinter.Button(top_frame, text = "Button1",bg = "#16a085" , fg = "red").pack()# 'fg - foreground' is used to color the contents
# btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()# 'text' is used to write the text on the Button
# btn3 = tkinter.Button(bottom_frame, text = "Button2", fg = "purple").pack(side = "left")# 'side' is used to align the widgets
# btn4 = tkinter.Button(bottom_frame, text = "Button2", fg = "orange").pack(side = "left")

# window.mainloop()