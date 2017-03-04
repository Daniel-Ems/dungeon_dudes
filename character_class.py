#!/usr/bin/env python3
import random
import sys
random.seed()

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
        """ Set the characters health """
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
        return '\n'.join(self.lootBag)

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
    monsterLoot = ["Clean Underwear", "A Jocks Baseball Cap", "Chewed Gum",
                   "Your Crushes Pom-Poms", "A Pocket-Protector",
                   "Half of a PB&J", "A Jocks Lunch Money",
                   "The First six Digits of Your Crushes Phone Number"]

    def __init__(self, location):
        self.location = location
        self.monsterList = []
        self.generateMonsters()
        self.lootOdds = 0

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
        return "".join(numMonsters)

    def generateMonsters(self):
        numMonsters = random.randint(1, 4)
        loot = random.randint(1, len(Room.monsterLoot))
        for monsters in range(numMonsters):
            monsterHealth = random.randint(1, 3)
            monsterStrength = random.randint(1, 3)
            monsterInitiative = random.randint(1, 6)
            monster = Monster(monsterHealth, monsterStrength,
                              monsterInitiative)
            monster.addLoot(Room.monsterLoot[loot-1])
            self.monsterList.append(monster)

    def popMonster(self):
        return self.monsterList.pop()

    def __str__(self):
        roomDetails = "{0}\n{1}"
        return roomDetails.format(self.location, self.getMonsters())


class Adventure:
    locations = ["The Bathroom", "The Arcade", "The Locker Room",
                 "The Football Field", "The Gym", "The Movie Theatre",
                 "The Parking Lot", "The Classroom", "The Mall",
                 "Your Crushes House", "The Diner", "The Playground"]

    def __init__(self, name, health, strength):
        self.hero = Hero(name, health, strength)
        self.map = []
        self.buildMap()
        self.room = 0
        self.monster = 0

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
            return attacker
        else:
            return defender

    def buildMap(self):
        numRooms = random.randint(6, 10)
        for number in range(numRooms):
            index = random.randint(1, len(Adventure.locations))
            room = Room(Adventure.locations.pop(index-1))
            self.map.append(room)

    def nextRoom(self):
        if len(self.map) == 0:
            self.room = 1
        else:
            self.room = self.map.pop()
            self.room.lootOdds = random.randint(1, 3)

    def nextMonster(self):
        if len(self.room.monsterList) == 0:
            self.monster = 1
        else:
            self.monster = self.room.popMonster()



