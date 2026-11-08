
import random
from classes.inventory import inventory


class Enemy:

    def __init__(self):
        self.inventory = inventory()
        self.isLost = False

    def takeCardsDeck(self, deck):
        if not deck:
            return None
        return self.inventory.takeCardsDeck(deck)

    def cardsCheck(self):
        return self.inventory.cardsCheck()

    def attack(self, table):
        if not self.inventory.cards:
            return None
        card = random.choice(self.inventory.cards)
        self.inventory.throwCard(card, table)
        print(f"Enemy attacks with: {card}")
        return card

    def defend(self, attack_card, table):
        possible_cards = [
            card for card in self.inventory.cards
            if card > attack_card
        ]
        if not possible_cards:
            print("Enemy cannot defend!")
            if table:
                self.inventory.takeCardTable(table)
            return None
        card = random.choice(possible_cards)
        self.inventory.throwCard(card, table)
        print(f"Enemy defends with: {card}")
        return card
        