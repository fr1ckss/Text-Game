import random
import sys
from enemy import Enemy

deck = []

for i in range(6, 15):
    deck.extend([i] * 4)

random.shuffle(deck)

table = []

sys.modules["main"] = sys.modules[__name__]
from player import Player

player = Player()
enemy = Enemy()

for i in range(6):
    player.takeCardsDeck()
    enemy.takeCardsDeck(deck)

while player.isLost == False:
    print("1 - Sprawdz karty")
    print("2 - Atak / broń się")
    print("3 - Wyjdz")