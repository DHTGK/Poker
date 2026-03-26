import random
import math
class Card:
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number
    
    def print(self):
        print(self.suite, self.number)

class Deck:
    deck = []
    drawn_cards = []

    def __init__(self):
        #make a full sized deck of cards
        for x in range (0, 4):
            for y in range (0, 13):
                if y == 0:
                    number = "Ace"
                elif y == 10:
                    number = "Jack"
                elif y == 11:
                    number = "Queen"
                elif y == 12:
                    number = "King"
                else:
                    number = str(y + 1)

                if x == 0:
                    suite = "Spade"
                elif x == 1:
                    suite = "Heart"
                elif x == 2:
                    suite = "Club"
                elif x == 3:
                    suite = "Diamond"

                self.deck.append(Card(number, suite))
                

    def draw(self):
        if len(self.deck) == 0:
            print("No Cards")
            return
        draw_number = random.randint(0, len(self.deck) - 1)

        card = self.deck[draw_number]
        self.deck.pop(draw_number)
        
        self.drawn_cards.append(card)

        card.print()

    def check(self):
        for x in range(0, len(self.deck)):
            current_card = self.deck[x]
            
            current_card.print()
    
    def reset(self):
        self.deck = self.deck + self.drawn_cards
        self.drawn_cards.clear()

Poker = Deck()