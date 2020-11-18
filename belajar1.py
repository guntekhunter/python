from tkinter import *

root = Tk()

# membuat label
label1 = Label(root, text="hello word!")
label2 = Label(root, text="ahhay")
#menampilkan ke layar
label1.grid(row=0, column=2)
label2.grid(row=1, column=1)

root.mainloop()