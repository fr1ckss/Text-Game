class Table:
    def __init__(self):
        self.cards = []

    def info(self):
        if self.cards == []:
            print("Na stole nie ma kart")
        else:
            print("Karty na stole:")
            for i, card in enumerate(self.cards):
                print(f"{i+1}: {card}")

    def discardCards(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)