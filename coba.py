from tkinter import *
root=Tk()

nilai1=Entry()
nilai2=Entry()
# menampilkan defauld teks pada form
# nilai1.insert(0, "masukkan nilai 1")
# nilai2.insert(0, "masikkan nilai 2")
nilai1.pack()
nilai2.pack()

def tambah():
    hasilnya = nilai1.get()+nilai2.get()
    muncul=Label(root, text="hasilnya adalah "+ hasilnya)
    muncul.pack()


hasil = Button(root, text="tambah", command=tambah)
hasil.pack()

root.mainloop()