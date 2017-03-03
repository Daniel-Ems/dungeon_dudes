#!/usr/bin/env python3


class Treasure:
    
    def __init__(self, title):
        self.title = title

    def __str__ (self):
        view = "{0}"
        return view.format(self.title)

def main():

    treasure = Treasure("Fresh Pair of Undies")

    print(str(treasure))

    

if __name__ == "__main__":
    main()
