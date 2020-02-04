import spell
import player
from random import randint

characterSpellSet00 = []
characterSpellSet01 = []
characterSpellSet02 = []
characterSpellSet = []
characters = []
player_01 = player.Player("",0, 0, 0, 0, 0, 0, characterSpellSet)
computer = player.Player("",0, 0, 0, 0, 0, 0, characterSpellSet)

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


character_00 = player.Player("Markov",100,100,10,10,9,1.5,characterSpellSet00)
character_01 = player.Player("Morrigan",100,100,10,10,10,1.5,characterSpellSet01)
character_02 = player.Player("Jaina",100,100,10,10,8,1.5,characterSpellSet02)

character_00.addSpellSet(basicAtack, spell_00, spell_01, spell_02)
character_01.addSpellSet(basicAtack, spell_03, spell_04, spell_05)
character_02.addSpellSet(basicAtack, spell_06, spell_07, spell_08)


characters.append(character_00)
characters.append(character_01)
characters.append(character_02)

#Seleciona um personagem para o jogador
def characterSelection():
    option = 0
    

    for i in range (len(characters)):
        print("[",i + 1,"] :")
        characters[i].printPlayerStats()

    print ("SELECT YOUR CHARACTER: \n")
    
    try:
        option = int (input())

        if(characters[option - 1]):
            p = characters[option - 1]
            return p

    except:
        print("INVALID VALUE!!!\n")
        characterSelection()

#Seleciona um personagem para o computador de modo aleatório e que seja diferente do personagem selecionado pelo jogador
def computerSelection(p):
    x = randint(0,2)
    c = characters[x]
    while c == p:
        x = randint(0,2)
        c = characters[x]
    return c

#"Lança um dado de 20 lados" que definira certas ações como acerto crítico e erro crítico
def rollDice():
    return randint(1, 20)

#Calcula o dano causado de acordo com os atributos dos personagens
def damage(x, y, s):
    dice = rollDice()
    
    if dice == 1:
        print(x.name ,"Miss!!!")
        return 0

    if dice == 20:
        damage = (x.atack + s.power - y.defense) * x.criticalDamage
        print("Critical Hit!!!", y.name,"lost ", damage, " heath points")
        return damage
    
    if dice > 1 and dice < 20:
        damage = (x.atack + s.power - y.defense) * 1
        print(y.name,"lost ", damage, " heath points")
        return damage
   
#Seleciona a ação do jogador
def playerAction(p):
    option = 0
    p.printSpellSet()
    try:
        option = int (input())

        if p.spells[option - 1]:

            if option == 1:
                p.mp = p.mp + 15
                if p.mp > 100:
                    p.mp = 100
                return p.spells[option - 1]
            if p.mp > p.spells[option - 1].cost:
                p.mp = p.mp - p.spells[option - 1].cost
                return p.spells[option - 1]
            else:
                print("Insufficient mana")
                playerAction(p)

    except:
        print("Insufficient mana")
        playerAction(p)

#Seleciona a ação do computador de modo aleatório se o computador não tiver mana suficiente ele executa uma ação pre progamada
def computerAction(c,count):
    x = randint(1,3)

    if c.mp < c.spells[x].cost:
        count = count + 1
        computerAction(c, count)

    if count == 3:
        return c.spells[0]
    
    c.mp = c.mp - c.spells[x].cost
    return c.spells[x]

#Define o turno
def turn(p, c):
    pSpell = playerAction(p)
    cSpell = computerAction(c, 0)
    
    if p.speed > c.speed:
        c.hp -= damage(p, c, pSpell)

        if c.hp > 0:
            p.hp = p.hp - damage(c, p, cSpell)

    if c.speed > p.speed:
        p.hp -= damage(c, p, cSpell)

        if p.hp > 0:
            c.hp = c.hp - damage(p, c, pSpell)
    
    if p.speed == c.speed:
        dice = rollDice()

        if dice <= 10:
            c.hp -= damage(p, c, pSpell)

            if c.hp > 0:
                p.hp = p.hp - damage(c, p, cSpell)

        if dice > 20:
            p.hp -= damage(c, p, pSpell)

            if c.hp > 0:
                c.hp = c.hp - damage(p, c, cSpell)

#Inicia a batalha entre jogador e computador
def battle(p, c):
    print(p.name," VS ", c.name)
    turnCount = 1
    while p.hp > 0 and c.hp > 0:
        print("Turn: ", turnCount)
        print(p.name ," ", p.hp, " / ", p.mp)
        print(c.name ," ", c.hp, " / ", c.mp, "\n")
        turn(p, c)
        print("\n")
        turnCount += 1

        if c.hp <= 0:
            print(p.name," Wins")

        if p.hp <= 0:
            print(c.name," Wins")
    
#main
def run():
    p = characterSelection()
    c = computerSelection(p)
    battle(p, c)