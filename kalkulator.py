from tkinter import *
root=Tk()
root.title("kalkulatornya agung")

masukkan=Entry(root, width=35, borderwidth=5)
masukkan.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(angka):
    # masukkan.delete(0, END)
    current = masukkan.get()
    masukkan.delete(0, END)
    masukkan.insert(0, str(current)+ str(angka))
def bersihkan():
    masukkan.delete(0,END)

def button_add():
    angka_pertama= masukkan.get()
    global num_pertama
    global kondisi
    kondisi="tambah"
    num_pertama=int(angka_pertama)
    masukkan.delete(0, END)
def samadengan():
    num_kedua=masukkan.get()
    masukkan.delete(0, END)
    if(kondisi=="kurang"):
        masukkan.insert(0, num_pertama-int(num_kedua))
    elif(kondisi=="tambah"):
        masukkan.insert(0, num_pertama+ int(num_kedua))
def kurang():
    angka_pertama= masukkan.get() 
    global num_pertama
    global kondisi
    kondisi="kurang"
    num_pertama=int(angka_pertama)
    masukkan.delete(0, END)
#     angka_kurang=masukkan.get()
#     global kurangnya
#     kurangnya=int(angka_kurang)
#     masukkan.delete(0, END)

tombol_1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
tombol_2 = Button(root, text="2", padx=40, pady=20, command=lambda : button_click(2))
tombol_3 = Button(root, text="3", padx=40, pady=20, command=lambda : button_click(3))
tombol_4 = Button(root, text="4", padx=40, pady=20, command=lambda : button_click(4))
tombol_5 = Button(root, text="5", padx=40, pady=20, command=lambda : button_click(5))
tombol_6 = Button(root, text="6", padx=40, pady=20, command=lambda : button_click(6))
tombol_7 = Button(root, text="7", padx=40, pady=20, command=lambda : button_click(7))
tombol_8 = Button(root, text="8", padx=40, pady=20, command=lambda : button_click(8))
tombol_9 = Button(root, text="9", padx=40, pady=20, command=lambda : button_click(9))
tombol_0 = Button(root, text="0", padx=40, pady=20, command=lambda : button_click(0))
tombol_tambah = Button(root, text="+", padx=41, pady=20, command= button_add)
tombol_kurang = Button(root, text="-", padx=41, pady=20, command=kurang)
tombol_samadengan = Button(root, text="=", padx=140, pady=20, command=samadengan)
tombol_bersihkan = Button(root, text="C", padx=140, pady=20, command=bersihkan)
#tampilan tombol

tombol_1.grid(row=1, column=0)
tombol_2.grid(row=1, column=1)
tombol_3.grid(row=1, column=2)

tombol_4.grid(row=2, column=0)
tombol_5.grid(row=2, column=1)
tombol_6.grid(row=2, column=2)

tombol_7.grid(row=3, column=0)
tombol_8.grid(row=3, column=1)
tombol_9.grid(row=3, column=2)

tombol_0.grid(row=4, column=1)
tombol_tambah.grid(row=4, column=0)
tombol_kurang.grid(row=4, column=2)
tombol_bersihkan.grid(row=6, column=0, columnspan=3)

tombol_samadengan.grid(row=5, column=0, columnspan=3)
root.mainloop()
