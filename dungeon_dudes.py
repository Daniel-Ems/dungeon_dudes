#!/usr/bin/env python3
import random


class Treasure:

    def __init__(self, title):
        self.title = title

    def __str__(self):
        view = "{0}"
        return view.format(self.title)


class Character:

    def __init__(self, health=0, strength=0, initiative=0):
        self.health = health
        self.strength = strength
        self.lootBag = []
        self.initiative = initiative

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

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, initiative):
        self._initiative = initiative
    
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
        super() .__init__(health, strength, 0)
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

    def __init__(self, health, strength, intiative):
        super() .__init__(health, strength, intiative)

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
            monsterInitiative = random.randint(1, 6)
            monster = Monster(monsterHealth, monsterStrength, monsterInitiative)
            self.monsterList.append(monster)

    def __str__(self):
        roomDetails = "{0}\n{1}"
        return roomDetails.format(self.location, self.getMonsters())

         
class Adventure:
    locations = ["The Bathroom", "The Arcade", "The Locker Room", "The \
Football Field", "The Gym", "The Movie Theatre", "The Parking Lot", "The \
Classroom", "The Mall", "Your Crushes House", "The Diner", "The Playground"]

    def __init__(self, hero):
        self.hero = hero
        self.map = []
        self.buildMap()
        self.level = 0

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

    def buildMap(self):
        numRooms = random.randint(8, 12)
        for number in range(numRooms):
            index = random.randint(1, len(Adventure.locations))
            room = Room(Adventure.locations.pop(index-1))
            self.map.append(room)

    def nextLevel(self):
        self.level = self.map.pop()
        

    
   
        

def main():
    random.seed()

    menuOptions = ["A: List items in the loot bag","B: Move to the next room",
                   "C: List your health", "D: List the monsters health", 
                   "E: Attack the Monster"]
    def menu(quest):
        while True:
            try:
                for items in menuOptions:
                    print(items)
                print("")
                userSelection = input("What would you like to do? ").lower()    
            except ValueError:
                print("Not today bossman")
                continue
            if userSelection not in ('a', 'b', 'c', 'd', 'e'):
                print("Try again slick")
                continue
            else:
                if userSelection == 'a':
                    print("Your loot:", hero.getLoot())
                if userSelection == 'b':
                    if quest.level == 0 or len(quest.level.monsterList) == 0:
                        quest.nextLevel()
                        nextRoom()
                    elif len(quest.level.monsterList) > 0:
                        print("No Running!")
                if userSelection == 'c':
                    print("Your health:", hero.health)
                if userSelection == 'd':
                    print("Monsters health:", monster.health)
                if userSelection == 'e':
                    battle()
            

        
    def battle():
        while(quest.level.monsterList):    
            monster = quest.level.popMonster()

            if hero.initiative >= monster.initiative:
                attack = hero
                defend = monster
            else:
                attack = monster
                defend = hero

            while(monster.health > 0 and hero.health > 0):
                quest.combat(attack, defend)
                if defend.health == 0:
                    break
                quest.combat(defend, attack)
                if defend.health == 0:
                    break

            if monster.health <= 0:
                print("congratulatons you killed the monster")
            else:
                print("you suck, you died")
                break


    def nextRoom():
        print("You have entered the magical world of " + quest.level.location)
        intro = "Watch out nerd! There are {0} jocks here!\n"
        print(intro.format(len(quest.level.monsterList)))
        
    heroName = input("Hey kid, what do you want to call your Hero? ")
    print("")
    hero = Hero(heroName, 10, 3)
    quest = Adventure(hero)

    menu(quest)

    hero.initiative = quest.diceRoll()
    

        
    


if __name__ == "__main__":
    main()
