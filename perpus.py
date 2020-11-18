class Moba:
    def __init__(self, skinName, skinHealth, skinSkill, skinDifence):
        self.name=skinName
        self.health=skinHealth
        self.skill=skinSkill
        self.difance=skinDifence 

    def serang(self, enemy):
        print (self.name+" serang "+ enemy.name)
        attack = self.skill/enemy.difance
        enemy.health-=attack
        print("darah tinggal: "+str(enemy.health))
    
    
hero1 = Moba("silong", 100, 70, 20)
hero2 =Moba("mia", 100, 60, 30)

hero1.serang(hero2)
hero2.serang(hero1)
hero1.serang(hero2)
hero2.serang(hero1)