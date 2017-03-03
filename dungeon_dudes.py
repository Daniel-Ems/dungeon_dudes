#!/usr/bin/env python3


class Treasure:
    
    def __init__(self, title):
        self.title = title

    def __str__ (self):
        view = "{0}"
        return view.format(self.title)

class Loot:

    def __init__(self):
        self.loot = []

    def addLoot(self, spoil):
        treasure = Treasure(spoil)
        self.loot.append(treasure)

    def __str__(self):
        result = []
        for items, spoils in enumerate(self.loot):
            result.append(str(spoils))
            result.append("\n")
        return "".join(result)

class Hero:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.loot = Loot()

    def addSpoils(self, spoils):
        self.loot.addLoot(spoils)

    def getSpoils(self):
        return str(self.loot)

def main():

    hero = Hero("Captain UnderPants")

    hero.addSpoils("Fresh Undies")
    hero.addSpoils("chewed gum")
    hero.addSpoils("condom wrapper")
    print(hero.getSpoils())
    
    

    

if __name__ == "__main__":
    main()
