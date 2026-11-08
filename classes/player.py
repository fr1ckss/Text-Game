from classes.inventory import Inventory

class Player:
    def __init__(self, table, deck, enemy=None):
        self.enemy = enemy
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

    def attack(self):
        if self.table.cards == []:
            print("\nTwoje karty: ")
            self.inventory.cardsCheck()
            choice_card = input("Wybierz kartę do ataku(wpisz wartosc karty):  ")
            if choice_card.isdigit():
                choice_card = int(choice_card)
                card_thrown = self.throwCard(choice_card)
                print(f"Zaatakowałeś kartą {card_thrown}.")
            else:
                print("Nieprawidłowa wartość karty. Spróbuj ponownie.")
                self.attack()

    def defend(self):
        if self.table.cards != []:
            self.table.info()
            print("\nTwoje karty: ")
            self.inventory.cardsCheck()
            print("Eśli chcesz spasować wpisz 'p' lub 'P'")
            choice_card = input("Wybierz kartę do obrony(wpisz wartosc karty):  ")
            if choice_card.isdigit():
                choice_card = int(choice_card)
                if choice_card < self.table.cards[0]:
                    print("Nie możesz obronić się tą kartą")
                    self.defend()
                elif choice_card > self.table.cards[0] or choice_card == self.table.cards[0]:
                    card_thrown = self.throwCard(choice_card)
                    print(f"Obroniłeś się kartą {card_thrown}. Karty z stołu zostały odłożone.")
                    self.wins_round += 1
                    self.table.discardCards()
                    self.takeCardsDeck()
                    self.enemy.takeCardsDeck()
            else:
                self.takeCardTable()
                print("Spasowałeś. Karty z stołu zostały zabrane do twojego ekwipunku.")
                self.enemy.wins_round += 1
                self.enemy.takeCardsDeck()