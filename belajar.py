#list iterable
timVollyA=["agung","jumaintang","samsuddin","kenta","thor"]
timVollyB=["anajay","jadi","ini","lagi","tidur","subuh"]

timVolly=[timVollyA,timVollyB]
for t in timVolly:
    for a in t :
        print(a)

angka = 0

while angka <=10:
    print("ini nilai ke-", angka+1)
    angka = angka + 1

jumlah = 20

while jumlah >10 and angka <=10:
    print("coba", jumlah)
    jumlah=jumlah-1
