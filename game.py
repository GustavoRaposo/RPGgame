import spell
import player
from random import randint

characterSpellSet00 = []
characterSpellSet01 = []
characterSpellSet02 = []
characterSpellSet = []
characters = []
player_01 = player.Player("",0, 0, 0, 0, 0, characterSpellSet)
computer = player.Player("",0, 0, 0, 0, 0, characterSpellSet)

basicAtack = spell.Spell("Chapuletada", 5, 0)
spell_00 = spell.Spell("Flames", 15, 10)
spell_01 = spell.Spell("Fire Bolt", 20, 20)
spell_02 = spell.Spell("Fireball", 30, 30)
spell_03 = spell.Spell("Frost Bite", 15, 10)
spell_04 = spell.Spell("Ice Spike", 20, 20)
spell_05 = spell.Spell("Ice Storm", 30, 30)
spell_06 = spell.Spell("Sparks", 15, 10)
spell_07 = spell.Spell("Lightning Bolt", 20, 20)
spell_08 = spell.Spell("Chain Lightning", 30, 30)


character_00 = player.Player("Markov",100,100,10,10,10,characterSpellSet00)
character_01 = player.Player("Morrigan",100,100,10,10,10,characterSpellSet01)
character_02 = player.Player("Jaina",100,100,10,10,10,characterSpellSet02)

character_00.addSpellSet(basicAtack, spell_00, spell_01, spell_02)
character_01.addSpellSet(basicAtack, spell_03, spell_04, spell_05)
character_02.addSpellSet(basicAtack, spell_06, spell_07, spell_08)


characters.append(character_00)
characters.append(character_01)
characters.append(character_02)


def characterSelection():
    option = 0
    

    for i in range (len(characters)):
        print("[",i + 1,"] :")
        characters[i].printPlayerStats()

    print ("SELECT YOUR CHARACTER: \n")
    
    try:
        option = int (input())

        if(characters[option - 1]):
            p1 = characters[option - 1]
            p1.printPlayerStats()
            return p1

    except:
        print("INVALID VALUE!!!\n")
        characterSelection()
    
def computerSelection(p1):
    x = randint(0,2)
    c = characters[x]
    while(c == p1):
        x = randint(0,2)
        c = characters[x]
    print("(----------------   VS   ----------------)")
    c.printPlayerStats()
    return c

def criticalHit():
    x = randint(0,10)
    if(x > 1):
        return 1
    print("Critical Hit!!!")
    return 1.5

def damage(x, y, s):
    damage = ((x.atack + s) * criticalHit()) - y.defense
    y.hp = y.hp - (((x.atack + s) * criticalHit()) - y.defense)
    print(y.name, " lost", damage, " health points!")
    return y.hp

def playerAction(p1, c):
    print("YOUR TURN!!!\n")
    print(p1.name, ": ",p1.hp, " HP/" , p1.mp, " MP\n")
    print("(----------------   VS   ----------------)")
    print(c.name, ": ",c.hp, " HP/" , c.mp, " MP\n")
    option = 0

    
    print("CHOOSE AN ACTION: \n")

    p1.printSpellSet()

    option = int (input())

    if(option == 1):
        print(p1.name, "CONJURED: ", c.spells[option - 1].name)
        damage(p1, c, p1.spells[option - 1].power)
        p1.mp += 15

        if (p1.mp > 100):
            p1.mp = 100

    if(option == 2):
        if(p1.mp > p1.spells[option - 1].cost):
            print(p1.name, "CONJURED: ", c.spells[option - 1].name)
            damage(p1, c, p1.spells[option - 1].power)
            p1.mp = p1.mp - p1.spells[option - 1].cost
        playerAction(p1, c)
        

    if(option == 3):
        if(p1.mp > p1.spells[option - 1].cost):
            print(p1.name, "CONJURED: ", c.spells[option - 1].name)
            damage(p1, c, p1.spells[option - 1].power)
            p1.mp = p1.mp - p1.spells[option - 1].cost
        playerAction(p1, c)

    if(option == 4):
        if(p1.mp > p1.spells[option - 1].cost):
            print(p1.name, "CONJURED: ", c.spells[option - 1].name)
            damage(p1, c, p1.spells[option - 1].power)
            p1.mp = p1.mp - p1.spells[option - 1].cost
        playerAction(p1, c)

def computerAction(c, p1):
    print("ENEMY TURN!!!\n")
    print(p1.name, ": ",p1.hp, " HP/" , p1.mp, " MP\n")
    print("(----------------   VS   ----------------)\n")
    print(c.name, ": ",c.hp, " HP/" , c.mp, " MP\n")
    
    x = randint(1,3)
    count = 0
    if(c.mp < c.spells[x].cost):
        count = count + 1
        computerAction(c, p1)

    if(count == 3):
        damage(c, p1, c.spells[0])
        print(c.name, "CONJURED: ", c.spells[0].name)
    print(c.name, "CONJURED: ", c.spells[x].name)
    damage(c, p1, c.spells[x].power)
    

def win(p1, c):
    if(p1.hp <= 0):
        print("YOU LOOSE!!!")
        return False
    if(c.hp <= 0):
        print("YOU WIN!!!")
        return False
    return True

def battle(p1, c):
    run = True
    while(run):
        if(p1.speed > c.speed):
            run = win(p1, c)
            playerAction(p1, c)
            run = win(p1, c)
            computerAction(c, p1)
            run = win(p1, c)

        if(p1.speed < c.speed):
            run = win(p1, c)
            computerAction(c, p1)
            run = win(p1, c)
            playerAction(p1,c)
            run = win(p1, c)

        if(p1.speed == c.speed):
            x = randint(1, 10)

            if(x <= 5):
                run = win(p1, c)
                playerAction(p1, c)
                run = win(p1, c)
                computerAction(c, p1)
                run = win(p1, c)

            if(x > 5):
                run = win(p1, c)
                computerAction(c, p1)
                run = win(p1, c)
                playerAction(p1, c)
                run = win(p1, c)

def start():
    p1 = characterSelection()
    c = computerSelection(p1)
    battle(p1, c)