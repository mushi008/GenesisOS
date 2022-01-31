import os
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Mushi Text Editor!')
root.iconbitmap('download.png')
root.geometry("1920x1080")

# Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Text Widget
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow",
               selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Scrollbar Configuration
text_scroll.config(command=my_text.yview())

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit())


root.mainloop()
