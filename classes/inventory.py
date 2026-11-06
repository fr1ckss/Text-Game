class inventory:
    def __init__(self):
        self.cards = []
        self.maxCard = 6

    def takeCardsDeck(self, deck):
        if len(self.cards) < self.maxCard:
            card = deck.pop()
            self.cards.append(card)
            return card
        else:
            print("Nie mozesz wziac wiecej kart")
            return None
    
    def takeCardTable(self, table):
        if table != []:
            card = table.pop()
            self.cards.append(card)
            return card
        else:
            print("Nie ma wiecej kart na stole")
            return None
    
    def throwCard(self, card, table):
        if card in self.cards:
            self.cards.remove(card)
            table.append(card)
            return card
        else:
            print("Nie masz takiej karty")
            return None

    def cardsCheck(self):
        for i, card in enumerate(self.cards):
            print(f"{i+1}: {card}")
