import random
from classes.player import Player
from classes.table import Table

deck = []

for i in range(6, 15):
    deck.extend([i] * 4)

random.shuffle(deck)
random.shuffle(deck)

table = Table()

enemy = Player(table, deck)
player = Player(table, deck, enemy)

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
        player.wins_round = 0
        enemy.wins_round = 0
        if player.inventory.cards == [] and deck == []:
            player.isLost = True
            print("Nie masz już kart i nie możesz dobrać nowych. Wygrałeś!")
        elif enemy.inventory.cards == [] and deck == []:
            enemy.isLost = True
            print("Przeciwnik nie ma już kart i nie może dobrać nowych. Przegrałeś!")

        if player.wins_round > enemy.wins_round or player.wins_round == enemy.wins_round:
            player.attack()
            enemy_defend()
        if enemy.wins_round > player.wins_round or player.wins_round == enemy.wins_round:
            enemy_attack()
            player.defend()

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

    


            

    
    
