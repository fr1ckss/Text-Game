import random

deck = []
for i in range(6, 15):
    deck.extend([i]*4)

table = []

player = Player()
enemy = Player()

def enemyPlayer(enemyInventory,table):
    if not enemyInventory.cards:
        return None
    chosenCard = random.choise(enemyInventory)
    enemyInventory.cards.remove(chosen_card)
    table.add_to_table(chosen_card)
    print(f"enemy throw card: {chosen_card}")
    return chosen_card
#in game:
playerInventory = Inventory()
enemyInventory = Inventory()
table = Table()
enemyMakeTurn(enemyInventory, table)

while player.isLost == False:
    print("1 - Sprawdz karty")
    print("2 - Atak / broń się")
    print("3 - Wyjdz")
    