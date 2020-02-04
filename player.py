class Player:
    def __init__(self, name, hp, mp, atack, defense, speed, criticalDamage, spells):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atack = atack
        self.defense = defense
        self.speed = speed
        self.criticalDamage = criticalDamage
        self.spells = []
    
    def addSpellSet(self, basicAtack, spell_0, spell_1, spell_2):
        self.spells.append(basicAtack)
        self.spells.append(spell_0)
        self.spells.append(spell_1)
        self.spells.append(spell_2)
    
    def printSpellSet(self):
        for i in range (len(self.spells)):
            print("        _________________________________\n",
                  "       |SPELL [",i+1,"]", "\n",
                  "       |      NAME  : ", self.spells[i].name, "\n",
                  "       |      COST  : ", self.spells[i].cost, " MP","\n",
                  "       _________________________________")
    
    def printPlayerStats(self):
        print("_____________________\n",
              "NAME  : ", self.name, "\n",
              "HP    : ", self.hp, "\n",
              "MP    : ", self.mp, "\n",
              "ATK   : ", self.atack, "\n",
              "DEF   : ", self.defense, "\n",
              "SPD   : ", self.speed)
        print("_____________________\n")