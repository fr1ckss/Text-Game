from classes.inventory import Inventory
from main import table, deck

class Player:
    def __init__(self):
        self.inventory = Inventory()
        self.isLost = False

    def takeCardsDeck(self):
        return self.inventory.takeCardsDeck(deck)
     
    def takeCardTable(self):
        return self.inventory.takeCardTable(table)
    
    def cardsCheck(self):
        return self.inventory.cardsCheck()
    
    def throwCard(self, card):
        return self.inventory.throwCard(card, table)
     