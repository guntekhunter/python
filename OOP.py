class Volly:
    def __init__(self, inputNama,power,jumping,smashing):
        self.nama=inputNama
        self.power=power
        self.jumping=jumping
        self.smashing=smashing

    def siapa(self):
        print("nama pemain adalah "+self.nama)
    
    def makan(self,up):
        self.power += up

    def minum(self):
        return self.power
posisi1 = Volly("agung",10,3,9)
posisi2 = Volly("Samsul",90,9,10)
posisi3 = Volly("Jumaintang",10,3,9)



posisi1.siapa()
posisi2.makan(10)
print(posisi2.minum())

# print(posisi2.nama)

# #print semua atribut

# print(posisi3.__dict__)