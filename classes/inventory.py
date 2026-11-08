class Inventory:
    def __init__(self, table, deck):
        self.cards = []
        self.maxCard = 6
        self.deck = deck
        self.table = table

    def takeCardsDeck(self):
        if len(self.cards) < self.maxCard and self.deck != []:
            for i in range(self.maxCard - len(self.cards)):
                card = self.deck.pop(i)
                self.cards.append(card)
            return True
        else:
            return None
    
    def takeCardTable(self):
        if self.table != []:
            for i in range(len(self.table.cards)):
                card = self.table.cards.pop(i)
                self.cards.append(card)
        else:
            return None
    
    def throwCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            self.table.addCard(card)
            return card
        else:
            return None

    def cardsCheck(self):
        if self.cards == []:
            return False
        else:
            for i, card in enumerate(self.cards):
                print(f"{i+1}: {card}")
            return True
