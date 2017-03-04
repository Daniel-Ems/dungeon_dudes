#!/usr/bin/env python3
import random
import sys
random.seed()


class Treasure:

    def __init__(self, title):
        # treasures title
        self.title = title

    def __str__(self):
        view = "{0}"
        return view.format(self.title)


class Character:

    def __init__(self, health=0, strength=0, initiative=0):
        # heallth of character
        self.health = health
        # strength of character
        self.strength = strength
        # characters lootbag
        self.lootBag = []
        # characters battle initiative
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
        """ Add loot to loot bag """
        self.lootBag.append(treasure)

    def __str__(self):
        playStats = "Players health: {0}\nPlayers Strength: {1}\n\
Players loot: \n{2}"
        return playStats.format(self.health, self.strength, self.getLoot())


class Hero(Character):

    def __init__(self, name, health, strength, initiative):
        # call parent class to handle paramters passed
        super() .__init__(health, strength, initiative)
        # set the hero's name
        self.name = name

    @property
    def name(self):
        """ The hero's name """
        return self._name

    @name.setter
    def name(self, name):
        """ set the hero's name """
        self._name = name

    def __str__(self):
        stats = "Heros Name: {0}\nHealth: {1}\nStrength: {2}\nGoodies:\n{3}"
        return stats.format(self.name, self.health, self.strength,
                            self.getLoot())


class Monster(Character):

    def __init__(self, health, strength, intiative):
        # call parent class to handle parameters passed
        super() .__init__(health, strength, intiative)

    def __str__(self):
        monsterStats = "Monster\nHealth: {0}\nStrength: {1}\n"
        return monsterStats.format(self.health, self.strength)


class Room:
    # Treasures to be dropped throughout game
    monsterLoot = ["Clean Underwear", "A Jocks Baseball Cap", "Chewed Gum",
                   "Your Crushes Pom-Poms", "A Pocket-Protector",
                   "Half of a PB&J", "A Jocks Lunch Money",
                   "The First six Digits of Your Crushes Phone Number"]

    def __init__(self, location):
        # the rooms location
        self.location = location
        # the rooms list of monsters
        self.monsterList = []
        # populates the monster list
        self.generateMonsters()
        # the odds a loot will be dropped in a room
        self.lootOdds = 0

    @property
    def location(self):
        """ The room's title """
        return self._location

    @location.setter
    def location(self, location):
        """ set the room's title """
        self._location = location

    def getMonsters(self):
        """ return the list of monsters """
        numMonsters = []
        # walk through list of monsters and join them into a string
        for number, monsters in enumerate(self.monsterList):
            numMonsters.append(str(monsters))
        return "".join(numMonsters)

    def generateMonsters(self):
        """ generates monsters for rooms """
        # randomlt generate the number of monsters per room, btw 1 and 4
        numMonsters = random.randint(1, 4)
        # randomly generate index for monsterLoot
        loot = random.randint(1, len(Room.monsterLoot))
        for monsters in range(numMonsters):
            # randomly assign monsters health
            monsterHealth = random.randint(1, 3)
            # randomly assign monsters strength
            monsterStrength = random.randint(1, 3)
            # randomly assign monsters initiative
            monsterInitiative = random.randint(1, 6)
            # create Monster
            monster = Monster(monsterHealth, monsterStrength,
                              monsterInitiative)
            # randomly assign loot to monster
            monster.addLoot(Room.monsterLoot[loot-1])
            self.monsterList.append(monster)

    def popMonster(self):
        """ pop off the next monster in the monster list """
        return self.monsterList.pop()

    def __str__(self):
        roomDetails = "{0}\n{1}"
        return roomDetails.format(self.location, self.getMonsters())


class Adventure:
    # room locations throughout the game
    locations = ["The Bathroom", "The Arcade", "The Locker Room",
                 "The Football Field", "The Gym", "The Movie Theatre",
                 "The Parking Lot", "The Classroom", "The Mall",
                 "Your Crushes House", "The Diner", "The Playground"]

    def __init__(self, name, health, strength, initiative):
        # A hero initiated in the adveneture
        self.hero = Hero(name, health, strength, initiative)
        # a list of room objects
        self.map = []
        # populates the map with rooms
        self.buildMap()
        # set to identify if there is a room loaded or no more rooms == 1
        self.room = 0
        # set to identify if there is a monster or not
        self.monster = 0

    def diceRoll(self):
        """ a single d6 roll """
        return random.randint(1, 6)

    def turnRoll(self, number):
        """ diceRolls depending on the strength of the characters passed """
        # used to store results
        result = []
        # roll the number of times as "number"
        for outcomes in range(number):
            # append results to result
            result.append(self.diceRoll())
        return result

    def combat(self, attacker, defender):
        """ posiitonal arguments passed that determines winner and loser """
        """ based of the die rolls and then returns the winner """
        # number of rolls == character strength
        offense = self.turnRoll(attacker.strength)
        defense = self.turnRoll(defender.strength)

        # the max of the two results compared, tie goes to the offense
        if max(offense) >= max(defense):
            """ return winner """
            return attacker
        else:
            return defender

    def buildMap(self):
        """ populate map with a random number of rooms """
        numRooms = random.randint(6, 10)
        for number in range(numRooms):
            # randomly assigna location from Adventure.locations
            index = random.randint(1, len(Adventure.locations))
            room = Room(Adventure.locations.pop(index-1))
            self.map.append(room)

    def nextRoom(self):
        """ pop the next room to enter from map """
        # if map is empty set room to 1 for win flag
        if len(self.map) == 0:
            self.room = 1
        else:
            # if rooms in map, pop next and assign loot odds
            self.room = self.map.pop()
            self.room.lootOdds = random.randint(1, 3)

    def nextMonster(self):
        """ pop the next monster to encounter """
        # if there are no more monsters in list set to 1 for win flag
        if len(self.room.monsterList) == 0:
            self.monster = 1
        else:
            # if there are monsters in list, pop next
            self.monster = self.room.popMonster()
