from tkinter import *

root = Tk()

def myClick():
    text = Label(root, text="anjir")
    text.pack()

tombol = Button(root, text="jangan di klik", 
padx=60,pady=10, command=myClick, fg="blue", bg="yellow")
tombol.pack()



root.mainloop()