#!/usr/bin/env python3


class Treasure:

    def __init__(self, title):
        self.title = title

    def __str__(self):
        view = "{0}"
        return view.format(self.title)


class Character:

    def __init__(self, health=0):
        self.health = health
        self.lootBag = []

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
        self._health -= 1

    def getSpoils(self):
        """ returns the contents of the loot bag """
        result = []
        for items, treasure in enumerate(self.lootBag):
            result.append(str(treasure))
            result.append("\n")
        return "".join(result)

    def __str__(self):
        characterStats = "Players health: {0}\nPlayers loot: \n{1}"
        characterStats.format(self.health, self.getSpoils())


class Hero(Character):

    def __init__(self, name, health):
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
        statistics = "Monster Health: {0}\nGoodies:\n{1}"
        return statistics.format(self.health, self.getSpoils())


def main():

    hero = Hero("Captain UnderPants", 10)

    hero.lootBag.append("Fresh Undies")
    hero.lootBag.append("chewed gum")
    hero.lootBag.append("capper")
    print(str(hero))

    monster = Monster(2)
    print(str(monster))


if __name__ == "__main__":
    main()
