from tkinter import *
root=Tk()

e = Entry(root)
e.pack()


def kirimkan():
    selamat = Label(root, text="Hello " + e.get())
    selamat.pack()

kirim = Button(root, text="masukkan nama anda", command=kirimkan)
kirim.pack()

root.mainloop()