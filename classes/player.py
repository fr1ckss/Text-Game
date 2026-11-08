from classes.inventory import Inventory

class Player:
    def __init__(self, table, deck):
        self.table = table
        self.deck = deck
        self.inventory = Inventory(self.table, self.deck)
        self.isLost = False
        self.wins_round = 0

    def takeCardsDeck(self):
        self.inventory.takeCardsDeck()
     
    def takeCardTable(self):
        self.inventory.takeCardTable()
    
    def cardsCheck(self):
        self.inventory.cardsCheck()
    
    def throwCard(self, card):
        return self.inventory.throwCard(card)
     