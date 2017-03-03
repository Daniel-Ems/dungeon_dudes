#!/usr/bin/env python3


class Treasure:

    def __init__(self, title):
        self.title = title

    def __str__(self):
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
        for items, treasure in enumerate(self.loot):
            result.append(str(treasure))
            result.append("\n")
        return "".join(result)


class Hero:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.loot = Loot()

    def addSpoils(self, treasure):
        """ Adds treasure to the loot bag """
        self.loot.addLoot(treasure)

    def getSpoils(self):
        """ returns the contents of the loot bag """
        return str(self.loot)

    def getHealth(self):
        """ The heros health """
        return self.health

    def decreaseHealth(self):
        """ Decrease the heros health when they loose a battle """
        self.health -= 1

    def __str__(self):
        statistics = "Heros Name: {0}\nHealth: {1}\nGoodies:\n{2}"
        return statistics.format(self.name, self.health, self.getSpoils())


def main():

    hero = Hero("Captain UnderPants")

    hero.addSpoils("Fresh Undies")
    hero.addSpoils("chewed gum")
    hero.addSpoils("condom wrapper")
    print(hero.getSpoils())
    print(hero.getHealth())
    hero.decreaseHealth()
    print(hero.getHealth())
    print(str(hero))


if __name__ == "__main__":
    main()
