import random

deck = []
for i in range(6, 15):
    deck.extend([i]*4)

table = []

player = Player()


while player.isLost == False:
    print(f"Twoji karty: {player.inventory.checkCards()}")
    