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
    # menuOptions contains the strings to be printed as menu options
    menuOptions = ["A: List items in the loot bag", "B: Move to the next room",
                   "C: List your health", "D: List the monsters health",
                   "E: Attack the Jock"]

    def menu(quest):
        # The while loop checks if the hero is alive, or there are no more
        # rooms
        while quest.hero.health > 0 and quest.room != 1:
            try:
                # This prints the menuOptions to the suer
                for items in menuOptions:
                    print(items)
                print("")
                # userSelection is user input validated by inputValidation
                userSelection = inputValidation("What do you want to do? ")
            except ValueError:
                print("Try again slick")
                continue
            # This ensures the users input is appropriate
            if userSelection not in ('a', 'b', 'c', 'd', 'e'):
                print("Try again slick")
                continue
            else:
                # if selected, the menu prints the contents of the hero's
                # loot bag
                if userSelection == 'a':
                    loot = "Your loot:\n{0}"
                    print(loot.format(quest.hero.getLoot()))
                    # if selected the menu takes the user to the next room, or
                    # staus in the current room
                if userSelection == 'b':
                    # If the game just started, or a room has no more monsters
                    if quest.room == 0 or quest.monster == 1:
                        quest.nextRoom()
                        exploreRoom()
                    # If there are still monsters in the room, a new room is
                    # not called
                    elif quest.monster.health > 0:
                        print("No Running!")
                # If selected, the menu prints users health
                if userSelection == 'c':
                    print("Your health:", quest.hero.health)
                # if selected the menu, will attemtp tp print the monsters
                # health
                if userSelection == 'd':
                    # error handling if there is no monster
                    if quest.monster == 0 or quest.monster == 1:
                        print("Don't wet your pants, your safe\n")
                    # This will print the health if there is a monster
                    else:
                        print("Jocks health:", quest.monster.health)
                # If selected the user will attempt to attack the monster
                if userSelection == 'e':
                    # If there are no monsters loaded, or they have been
                    # defeated, this will print accordingly
                    if quest.monster == 0 or quest.monster == 1:
                        print("There's no one to noogie, Psycho\n")
                    # If there is a monster the user is sent to battle.
                    else:
                        # This will take the user to the battle function
                        battle()

    def battle():
        # The condition is set to loop through all monsters in the room
        while(quest.monster != 1):
            # setting monster for readability in function
            monster = quest.monster
            # setting hero for readability in function
            hero = quest.hero
            # if lootOdds is used to randomply drop treasures throughout rooms
            lootOdds = random.randint(1, 3)
            # This will check users initiative vs monsters, and set
            # appropriately
            if hero.initiative >= monster.initiative:
                attacker = hero
                defender = monster
            else:
                attacker = monster
                defender = hero
            # The condition is set until either the monster or hero dies
            while(monster.health > 0 and hero.health > 0):
                # This format string will print health updates to the user
                hpUpdate = "Your Health: {0}\nJock Health: {1}"
                # winner is the winner of the quest.combat
                winner = quest.combat(attacker, defender)
                # The following will check whether the winner was the hero or
                # the jock. It will then update health and print statements
                # appropriately depending on the the results of the combat
                # and who was attacking or defending
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
                # If the defender dies in the middle of battle do not continue
                if defender.health == 0:
                    break
                # The following will check whether the winner was the hero or
                # the jock. It will then update health and print statements
                # appropriately depending on the the results of the combat
                # and who was attacking or defending
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
                # if the attacker dies in battle do not continue
                if attacker.health == 0:
                    break
            # This will print the health update format
            print(hpUpdate.format(quest.hero.health, quest.monster.health),
                  "\n")
            # load the next monster
            quest.nextMonster()
            # Win Case, if the monster's health drops to 0 the user wins.
            if monster.health <= 0:
                print("Conratulations you knocked out the Jock!\n")
                # if lootOdds in battle match lootOdds in room, treasure is 
                # droped
                if lootOdds == quest.room.lootOdds:
                    # This adds the loot from the monster to the hero's lootbag
                    quest.hero.addLoot(monster.getLoot())
                    # format string used to print treasure recieved
                    spoils = "You are now the proud owner of {0}!\n"
                    print(spoils.format(monster.getLoot()))
                break
            # Break loop because the user died
            else:
                break
        # This notifies the user they have completed their current location
        if quest.monster == 1 and hero.health != 0:
            levelComplete = "Congrats Dweeb, you defeated the {0}!"
            print(levelComplete.format(quest.room.location))

    def exploreRoom():
        # If there is a room
        if quest.room != 1:
            # format string that prints a welcome and the location name"
            intro = ("You have entered the magical world of {0}!\n"
                     "Watch out Nerd! There {1} here!\n")
            # recieve the number of monsters in the room
            numMonsters = len(quest.room.monsterList)
            if numMonsters == 1:
                # modified print statement for singular jock
                print(intro.format(quest.room.location, "is 1 Jock"))
            else:
                multMonsters = "are {0} Jocks"
                # print the number of jocks in the room
                print(intro.format(quest.room.location,
                      multMonsters.format(numMonsters)))
            # load the rooms first monster
            quest.nextMonster()
            # Set the users initiative for new room
            # quest.hero.inititative = 
            x = quest.diceRoll()
            print("debug", x)
            print("iniitiative debug: ", quest.hero.initiative)

    def inputValidation(string):
        # continue to loop until condition is met
        while True:
            try:
                # assign the string passed to the function to "input"
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
    
    # Let the user type the hero's name
    heroName = inputValidation("Hey kid, what do you want to call your Hero? ")

    # Create an adventure called quest, passeing the hero's name, health and
    # strength 
    quest = Adventure(heroName, 10, 3)

    menu(quest)

    if quest.hero.health == 0:
        print("You came.. You saw... They wedgied you to death")
    if quest.room == 1:
        print("Congratulations! You beat up all the Jocks!")


if __name__ == "__main__":
    main()
