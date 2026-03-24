import random
import math
class Card:
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number
    
    def print(self):
        if self.suite == 0:
            suite = "Club"
        elif self.suite == 1:
            suite = "Heart"
        elif self.suite == 2:
            suite = "Spade"
        elif self.suite == 3:
            suite = "Diamond"
        
        if self.number == 1:
            number = "Ace"
        elif self.number == 11:
            number = "Jack"
        elif self.number == 12:
            number = "Queen"
        elif self.number == 13:
            number = "King"
        else:
            number = str(self.number)

        print(suite, number)

class Deck:
    deck = [1] * 52
    count = 52

    def draw(self):
        card = random.randint(0, 51)

        suite = math.floor(card / 13)
        card_number = (card - (suite * 13)) + 1

        return Card(suite, card_number)

    def check(self):
        for x in range(0, 52):
            card = x

            suite = math.floor(card / 13)
            card_number = (card - (suite * 13)) + 1
            
            current_card = Card(suite, card_number)
            
            current_card.print()
    
    def reset(self):
        for x in self.deck:
            x = 1
        count = 52

Poker = Deck()
Poker.check()
Poker.reset()