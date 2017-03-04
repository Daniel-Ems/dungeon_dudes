#!/usr/bin/env python3
import random
import sys  
from character_class import Treasure
from character_class import Character
from character_class import Hero
from character_class import Monster
from character_class import Room
from character_class import Adventure




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
