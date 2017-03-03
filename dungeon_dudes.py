#!/usr/bin/env python3
import random


class Treasure:

    def __init__(self, title):
        self.title = title

    def __str__(self):
        view = "{0}"
        return view.format(self.title)


class Character:

    def __init__(self, health=0, strength=0):
        self.health = health
        self.strength = strength
        self.lootBag = []

    @property
    def health(self):
        """ The characters health """
        return self._health

    @health.setter
    def health(self, health):
        """ Set the charachters health """
        self._health = health

    @property
    def strength(self):
        """ the charaters strength """
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Set the Characters strength """
        self._strength = strength

    def decreaseHealth(self):
        """ Decrease health when they loose a battle """
        self._health -= 1

    def getLoot(self):
        """ returns the contents of the loot bag """
        result = []
        for items, treasure in enumerate(self.lootBag):
            result.append(str(treasure))
            result.append("\n")
        return "".join(result)

    def addLoot(self, treasure):
            self.lootBag.append(treasure)

    def __str__(self):
        playStats = "Players health: {0}\nPlayers Strength: {1}\n\
Players loot: \n{2}"
        return playStats.format(self.health, self.strength, self.getLoot())


class Hero(Character):

    def __init__(self, name, health, strength):
        super() .__init__(health, strength)
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        stats = "Heros Name: {0}\nHealth: {1}\nStrength: {2}\nGoodies:\n{3}"
        return stats.format(self.name, self.health, self.strength,
                            self.getLoot())


class Monster(Character):

    def __init__(self, health, strength):
        super() .__init__(health, strength)

    def __str__(self):
        monsterStats = "Monster\nHealth: {0}\nStrength: {1}\n"
        return monsterStats.format(self.health, self.strength)


class Room:

    def __init__(self, location):
        self.location = location
        self.monsterList = []
        self.generateMonsters()

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    def getMonsters(self):
        numMonsters = []
        for number, monsters in enumerate(self.monsterList):
            numMonsters.append(str(monsters))
            numMonsters.append("\n")
        return "".join(numMonsters)

    def popMonster(self):
        return self.monsterList.pop()

    def generateMonsters(self):
        numMonsters = random.randint(1, 6)
        for monsters in range(numMonsters):
            monsterHealth = random.randint(1, 3)
            monsterStrength = random.randint(1, 3)
            monster = Monster(monsterHealth, monsterStrength)
            self.monsterList.append(monster)

    def __str__(self):
        roomDetails = "{0}\n{1}"
        return roomDetails.format(self.location, self.getMonsters())


class Adventure:                 

    def __init__(self, hero):
        self.hero = hero

    def diceRoll(self):
        return random.randint(1, 6)

    def turnRoll(self, number):
        result = []
        for outcomes in range(number):
            result.append(self.diceRoll())
        return result

    def combat(self, attacker, defender):

        offense = self.turnRoll(attacker.strength)
        defense = self.turnRoll(defender.strength)

        if max(offense) >= max(defense):
            defender.decreaseHealth()
            print(str(defender))

    
   
        

def main():
    random.seed()
"""
    def menu():
        menuOptions = ["A: List items in the loot bag", "B: Move to the next \
location", "C: list out your health", "D: List out monsters health", "E: Attack\
the monster"]
        for options in menuOptions:
            print(options)
        while True:
            try:
                userInput.islower() = input("What would you like to do? ")
        except ValueError:
            print("C'mon kid, you wanna play or not?")
            continue

        if  userInput not in ('a', 'b', 'c', 'd', 'e'):
            print("Try again dude, your not that clever")
            continue 

        else:
            if userInput is 'a':
                print(Hero.getLoot)
            if userInput is 'b':
"""   

    heroName = input("Hey kid, what do you want to call your Hero? ")
 
    menu()
    hero = Hero(heroName, 10, 3)
    quest = Adventure(hero)

    room = Room("The bathroom")

    monster = room.popMonster()

    initiative = quest.turnRoll(2)

    if initiative[0] >= initiative[1]:
        first = hero
        second = monster
    else:
        first = monster
        second = hero

    while(monster.health > 0 and hero.health > 0):
        quest.combat(first, second)
        if second.health == 0:
            break
        quest.combat(second, first)
        if first.health == 0:
            break

    if monster.health <= 0:
        print("congratulatons you killed the monster")
    else:
        print("you suck, you died")
        
    


if __name__ == "__main__":
    main()
