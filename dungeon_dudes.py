#!/usr/bin/env python3


class Treasure:
    
    def __init__(self, title):
        self.title = title

    def __str__ (self):
        view = "{0}"
        print("creating treasure")
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

def main():

    lootbag = Loot()
    lootbag.addLoot("Fresh Undies")
    lootbag.addLoot("chewed gum")
    lootbag.addLoot("condom wrapper")
    print(str(lootbag))
    
    

    

if __name__ == "__main__":
    main()
