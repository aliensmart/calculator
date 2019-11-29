from tkinter import *

window = Tk()
window.title("drop Down Menu")


def funct():
    pass

#Creating a root menu to insert all the sub menus

root_menu = Menu(window)
window.config(menu = root_menu)


#creating sub menu in the root menu

file_menu = Menu(root_menu) # it initializes a new su menu in the root menu
root_menu.add_cascade(label = "File", menu = file_menu) # it creates the name of the sub menu
file_menu.add_command(label = "new file...", command = funct) #it adds a option to the sub menu
file_menu.add_command(label = "open File", command = funct) 
file_menu.add_separator()# it adds a line after the openfile option
file_menu.add_command(label = "exit", command = window.quit)


#creatin a new sub menu
edit_menu = Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = funct)
edit_menu.add_command(label = "Redo", command = funct)

window.mainloop()