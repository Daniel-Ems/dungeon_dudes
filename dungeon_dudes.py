#!/usr/bin/env python3
import random
import sys


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
        numMonsters = random.randint(1, 1)
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
        numRooms = random.randint(1, 2)
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


def main():
    random.seed()

    menuOptions = ["A: List items in the loot bag", "B: Move to the next room",
                   "C: List your health", "D: List the monsters health",
                   "E: Attack the Jock"]

    def menu(quest):
        while quest.hero.health > 0 and quest.room != 1:
            try:
                for items in menuOptions:
                    print(items)
                print("")
                userSelection = inputValidation("What do you want to do? ")
            except ValueError:
                print("Try again slick")
                continue
            if userSelection not in ('a', 'b', 'c', 'd', 'e'):
                print("Try again slick")
                continue
            else:
                if userSelection == 'a':
                    loot = "Your loot:\n{0}"
                    print(loot.format(quest.hero.getLoot()))

                if userSelection == 'b':
                    if quest.room == 0 or quest.monster == 1:
                        quest.nextRoom()
                        exploreRoom()
                    elif quest.monster.health > 0:
                        print("No Running!")
                if userSelection == 'c':
                    print("Your health:", quest.hero.health)
                if userSelection == 'd':
                    if quest.monster == 0:
                        print("Don't wet your pants, your safe\n")
                    elif quest.monster == 1:
                        print("They are gone sweetie, don't worry\n")
                    else:
                        print("Jocks health:", quest.monster.health)
                if userSelection == 'e':
                    if quest.monster == 0:
                        print("There's no one to noogie, Psycho\n")
                    elif quest.monster == 1:
                        print("Take a breath, you already won\n")
                    else:
                        battle()

    def battle():
        while(quest.monster != 1):
            monster = quest.monster
            lootOdds = random.randint(1, 3)
            hero = quest.hero
            if hero.initiative >= monster.initiative:
                attacker = hero
                defender = monster
            else:
                attacker = monster
                defender = hero

            while(monster.health > 0 and hero.health > 0):
                hpUpdate = "Your Health: {0}\nJock Health: {1}"
                winner = quest.combat(attacker, defender)
                if winner == attacker and attacker == hero:
                    print("Your wedgie was successful! The Jock lost 1 hp")
                    quest.monster.decreaseHealth()
                elif winner == defender and defender == hero:
                    print("The Jock tried to give you a swirly! He missed!")
                elif winner == attacker and attacker == monster:
                    print("The Jocks swirly made you cry and lose 1 hp")
                    quest.hero.decreaseHealth()
                else:
                    print("You tried to give the Jock a wedgie. You missed!")
                if defender.health == 0:
                    break

                winner = quest.combat(defender, attacker)
                if winner == attacker and attacker == hero:
                    print("The Jock tried to give you a swirly! He missed!")
                elif winner == defender and defender == hero:
                    print("Your wedgie was successful! The Jock lost 1 hp")
                    quest.monster.decreaseHealth()
                elif winner == attacker and attacker == monster:
                    print("You tried to give the Jock a wedgie. You missed!")
                else:
                    print("The Jocks swirly made you cry and lose 1 hp")
                    quest.hero.decreaseHealth()
                print(hpUpdate.format(quest.hero.health, quest.monster.health),
                      "\n")
                if attacker.health == 0:
                    break

            quest.nextMonster()
            if monster.health <= 0:
                print("Conratulations you knocked out the Jock!\n")
                if lootOdds == quest.room.lootOdds:
                    quest.hero.addLoot(monster.getLoot())
                    spoils = "You are now the proud owner of {0}!\n"
                    print(spoils.format(monster.getLoot()))
                break
            else:
                break

        if quest.monster == 1 and hero.health != 0:
            levelComplete = "Congrats Dweeb, you defeated the {0}!"
            print(levelComplete.format(quest.room.location))

    def exploreRoom():
        if quest.room != 1:
            intro = ("You have entered the magical world of {0}!\n"
                     "Watch out Nerd! There {1} here!\n")
            numMonsters = len(quest.room.monsterList)
            if numMonsters == 1:
                print(intro.format(quest.room.location, "is 1 Jock"))
            else:
                multMonsters = "are {0} Jocks"
                print(intro.format(quest.room.location,
                      multMonsters.format(numMonsters)))
            quest.nextMonster()

    string = "Hey kid, what do you want to call your Hero? "

    def inputValidation(string):
        while True:
            try:
                userInput = input(string)
                print("")
            except ValueError:
                print("Try again slick")
                continue
            except KeyboardInterrupt:
                print("\nSo long NERD!")
                sys.exit()
            except EOFError:
                print("\nNot on my watch!")
                sys.exit()
            return userInput

    heroName = inputValidation(string)

    quest = Adventure(heroName, 10, 3)

    quest.hero.initiative = quest.diceRoll()
    menu(quest)

    if quest.hero.health == 0:
        print("You came.. You saw... They wedgied you to death")
    if quest.room == 1:
        print("Congratulations! You beat up all the Jocks!")


if __name__ == "__main__":
    main()
