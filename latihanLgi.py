class Hero:
    def __init__(self, nama, attack, difence, health):
        self.__name=nama
        self.__attack=attack
        self.__difence=difence
        self.__health=health

    def getNama(self):
        return self.__name

    def pukul(self,lawan):
        print(self.getNama()+" Memukul "+lawan.getNama())
        lawan.__health-= self.__attack
        lawan.__health+= lawan.__difence
        print(lawan.__health)
        

        
    

naruto=Hero("naruto", 70, 10, 250)
sasuke=Hero("sasuke", 50, 20, 200)

naruto.pukul(sasuke)