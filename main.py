import random
from classes.player import Player
from classes.table import Table

deck = []

for i in range(6, 15):
    deck.extend([i] * 4)

random.shuffle(deck)

random.shuffle(deck)

table = Table()

player = Player(table, deck)
enemy = Player(table, deck)

def  player_attack():
    if table.cards == []:
        player.cardsCheck()
        choice_card = int(input("Wybierz kartę do ataku(wpisz wartosc karty):  "))
        card_thrown = player.throwCard(choice_card)
        print(f"Zaatakowałeś kartą {card_thrown}.")

def player_defend():
    if table.cards != []:
        table.info()
        print("\nTwoje karty: ")
        player.cardsCheck()
        choice_card = input("Wybierz kartę do obrony(wpisz wartosc karty):  ")
        if choice_card.isdigit():
            choice_card = int(choice_card)
            if choice_card < table.cards[0]:
                print("Nie możesz obronić się tą kartą")
                player.defend()
            elif choice_card > table.cards[0] or choice_card == table.cards[0]:
                card_thrown = player.throwCard(choice_card)
                print(f"Obroniłeś się kartą {card_thrown}. Karty z stołu zostały odłożone.")
                player.wins_round += 1
                table.discardCards()
                player.takeCardsDeck()
                enemy.takeCardsDeck()
        else:
            player.takeCardTable()
            print("Spasowałeś. Karty z stołu zostały zabrane do twojego ekwipunku.")
            enemy.wins_round += 1
            enemy.takeCardsDeck()

    # if table.cards == []:
    #     choice_card = input("Wybierz kartę do ataku(wpisz wartosc karty):  ")
    #     card_thrown = player.throwCard(choice_card, table)
    # else:
    #     print(f"Wybierz kartę lub spasuj.")
    #     choice_card = input("Wybierz kartę do obrony(wpisz wartosc karty):  ")
    #     if choice_card < table.cards[0]:
    #         print("Nie możesz obronić się tą kartą")
    #     elif choice_card > table.cards[0] or choice_card == table.cards[0]:
    #         card_thrown = player.throwCard(choice_card, table)
    #         print(f"Obroniłeś się kartą {card_thrown}. Karty z stołu zostały odłożone.")
    #         player.wins_round += 1
    #         table.discardCards()
    #     else: 
    #         player.takeCardTable()
    #         print("Spasowałeś. Karty z stołu zostały zabrane do twojego ekwipunku.")
    #         enemy.wins_round += 1
    #         enemy.takeCardsDeck()

def enemy_attack():
    enemy_choice_card = random.choice(enemy.inventory.cards)
    if table.cards == []:
        card_thrown = enemy.throwCard(enemy_choice_card)
        print(f"Przeciwnik zaatakował kartą {card_thrown}.")

def enemy_defend():
    enemy_choice_card = random.choice(enemy.inventory.cards)
    if table.cards != []:
        if enemy_choice_card < table.cards[0]:
            print("Przeciwnik spasował. Karty z stołu zostały zabrane do jego ekwipunku.")
            player.wins_round += 1
            enemy.takeCardTable()
            player.takeCardsDeck()
        elif enemy_choice_card > table.cards[0] or enemy_choice_card == table.cards[0]:
            card_thrown = enemy.throwCard(enemy_choice_card)
            print(f"Przeciwnik obronił się kartą {card_thrown}. Karty z stołu zostały odłożone.")
            enemy.wins_round += 1
            table.discardCards()
            player.takeCardsDeck()
            enemy.takeCardsDeck()
        else: 
            enemy.takeCardTable()
            print("Przeciwnik spasował. Karty z stołu zostały zabrane do jego ekwipunku.")
            player.wins_round += 1
            player.takeCardsDeck()

def round():

    while player.isLost == False or enemy.isLost == False:
        if player.inventory.cards == [] and deck == []:
            player.isLost = True
            print("Nie masz już kart i nie możesz dobrać nowych. Wygrałeś!")
        elif enemy.inventory.cards == [] and deck == []:
            enemy.isLost = True
            print("Przeciwnik nie ma już kart i nie może dobrać nowych. Przegrałeś!")

        if player.wins_round > enemy.wins_round or player.wins_round == enemy.wins_round:
            player_attack()
            enemy_defend()
        elif enemy.wins_round > player.wins_round or player.wins_round == enemy.wins_round:
            enemy_attack()
            player_defend()
    

player = Player()
enemy = Player()

for i in range(6):
    player.takeCardsDeck()
    enemy.takeCardsDeck(deck)

    # for card in table:
    #     table.info()

    #     if card_thrown > card:
    #         print("Wygrałeś rundę!")
    #         player.wins_round += 1
    #     elif card_thrown == card:
    #         print("Remis!")
    #         player.wins_round += 1
    #         enemy.wins_round += 1
player.takeCardsDeck()
enemy.takeCardsDeck()


while True:
    print("1 - Zacznij rundę")
    print("2 - Wyjdz")
    choice = input("Wybierz akcję: ")
    if choice == "1":
        round()
    else:
        print("Wyjście z gry...")
        break

    


            

    
    
