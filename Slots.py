import random

slot_images = ["A", "K", "Q", "J", "10", "Wild"]

# Setting up the player then the Slots machine classes

class Player:
    def __init__(self, money):
        self.money = money


class Slots:
    def __init__(self, multiplier, bet, lines=3):
        self.multiplier = multiplier
        self.bet = bet
        self.line = lines
        self.line_1 = None
        self.line_2 = None
        self.line_3 = None

    def roll3(self):
        self.line_1 = random.choice(slot_images)
        self.line_2 = random.choice(slot_images)
        self.line_3 = random.choice(slot_images)


player1 = Player(1000)
slot1 = Slots(1, 50)
slot1.roll3()
player1.money -= slot1.bet
print(slot1.line_1, slot1.line_2, slot1.line_3)

# Starting the hell of making the checks...

if slot1.line_1 == slot1.line_2 and slot1.line_2 == slot1.line_3:
    print("JACKPOT!!!")
    if slot1.line_1 == "A":
        player1.money += slot1.bet * 10
    elif slot1.line_1 == "K":
        player1.money += slot1.bet * 7
    elif slot1.line_1 == "Q":
        player1.money += slot1.bet * 5
    elif slot1.line_1 == "J":
        player1.money += slot1.bet * 3
    elif slot1.line_1 == "10":
        player1.money += slot1.bet * 2
    elif slot1.line_1 == "Wild":
        print("WTF player...")
        player1.money += slot1.bet * 100
if slot1.line_1 == "10" and slot1.line_2 == "J" and slot1.line_3 == "Q":
    print("Winner")
    player1.money += slot1.bet * 1.1
if slot1.line_1 == "J" and slot1.line_2 == "Q" and slot1.line_3 == "K":
    print("Winner")
    player1.money += slot1.bet * 1.2
if slot1.line_1 == "Q" and slot1.line_2 == "K" and slot1.line_3 == "A":
    print("Winner")
    player1.money += slot1.bet * 1.5


print(player1.money)
