import random


coin = random.choice(["Red", "Black"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["jack", "A c e", "King", "Queen", "Jocker", "Diamond", "Deuces", "Spades", "Clover", "Hearts"]
random.shuffle(cards)
for card in cards:
    print(card)