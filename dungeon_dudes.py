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

class Character:

    def __init__(self, health = 0):
        self.health = health
        self.lootBag = Loot()

    @property
    def health(self):
        """ The characters health """
        return self._health

    @health.setter
    def health(self, health):
        """ Set the charachters health """
        self._health = health

    def decreaseHealth(self):
        """ Decrease health when they loose a battle """
        self.health -= 1

    def addSpoils(self, treasure):
        """ Adds treasure to the loot bag """
        self.lootBag.addLoot(treasure)

    def getSpoils(self):
        """ returns the contents of the loot bag """
        return str(self.lootBag)

        
        

class Hero(Character):

    def __init__(self, name , health):
        super() .__init__(health)
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        statistics = "Heros Name: {0}\nHealth: {1}\nGoodies:\n{2}"
        return statistics.format(self.name, self.health, self.getSpoils())

class Monster(Character):

    def __init__(self, health):
        super() .__init__(health)

    def __str__(self):
        statistics = "Monster Health: {0}\nGoodies:\n{2}"
        return statistics.format(self.name, self.health, self.getSpoils())
        


def main():

    hero = Hero("Captain UnderPants", 10)

    hero.addSpoils("Fresh Undies")
    hero.addSpoils("chewed gum")
    hero.addSpoils("condom wrapper")
    print(str(hero))
    


if __name__ == "__main__":
    main()
