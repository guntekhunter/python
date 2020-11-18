import random
#pus=========================================
print("puskesmas")
pus=input("puskesmas :")
kata=["batu","gunting","kertas"]
generator = random.choice(kata)
print("lawan:", generator) 
if pus is generator:
    print("seri")
#elif pus == "batu" and generator == "kertas":
#    print("kalah")

#batu
elif pus == "batu":
    if generator == "kertas":
        print("kalah")
    else:
        print("menang")
#gunting
elif pus == "gunting":
    if generator == "kertas":
        print("menang")
    else:
        print("kalah")  
#kertas
elif pus == "kertas":
    if generator == "batu":
        print("menang")
    else:
        print("kalah")
else:
    print("you're input is wrong!")

    


