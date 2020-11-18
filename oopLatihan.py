class Volly:
    def __init__(self, name, power, spike, jump, passing, health):
        self.nama = name
        self.kekuatan = power
        self.pukul = spike
        self.lompat = jump
        self.passing = passing
        self.sehat = health

    # def serpis(self,Kurang):
    #     self.health -= Kurang
    def serang(self, lawan):
        print(self.nama+" Menyerang "+lawan.nama)
        lawan.diserang(self, self.kekuatan)

    def diserang(self, lawan, kekerasan):
        print(self.nama+" diserang " + lawan.nama)
        pukulan_diterima = kekerasan/self.passing
        print("diterima kekuatan:"+str(pukulan_diterima))
        self.sehat -= pukulan_diterima
        print("darah "+self.nama+" adalah: "+str(self.sehat))




anggota1 = Volly("agung", 10, 5, 8, 9, 100)
anggota1=Volly("samslu", 12,129,2,0, 90)
anggota2 = Volly("samsul", 10, 7, 6, 10, 100)

anggota1.serang(anggota1)


    