import Deck

class Player:
    def __init__(self):
        cash = 10,000
        hand = []

    def print_money(self):
        print(self.cash)
    
    def bet_money(self, amount):
        cash -= amount

    def clear_hand(self):
        self.hand = []

    def add_hand(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(self.hand)

    def return_cards(self):
        print("Write 1 for each card you want to return and 0 for the ones you don't, seperated by spaces.")

        #check for valid true and false
        debug = True
        while debug == True:
            one, two, three, four, five = input().split

            if (one == 1 or one == 0) and (two == 1 or two == 0) and (three == 1 or three == 0) and (four == 1 or four == 0) and (five == 1 or five == 0):
                debug == False
            else:
                print("Not a valid input.")

        #remove cards from hand
        count = 0
        for x in range(0, 4):
            if x == 0 and one == True:
                self.hand.pop(x)
                count += 1
            if x == 1 and two == True:
                self.hand.pop(x)
                count += 1
            if x == 2 and three == True:
                self.hand.pop(x)
                count += 1
            if x == 3 and four == True:
                self.hand.pop(x)
                count += 1
            if x == 4 and five == True:
                self.hand.pop(x)
                count += 1

        return count


class Poker:
    pot = 0
    def __init__(self):
        self.deck = Deck()
        self.community_cards = []
        self.player = Player()

    def hand_value(self, cards):
        current_max = 1
        current_high_card = cards[0].give_number

        for x in range(0, 13):
            if x == 0:
                    number = "Ace"
            elif x == 10:
                number = "Jack"
            elif x == 11:
                number = "Queen"
            elif x == 12:
                number = "King"
            else:
                number = str(y + 1)

            count = 0
            for y in range(0, 4):
                if cards[y].give_number() == number:
                    count += 1
                if current_max < count:
                    current_max = count
                    current_high_card = number
                elif current_max == count:
                    

Game = Poker()
#initial bet
Poker.player.bet_money(100)
Poker.pot += 100

#give player 5 cards and place 5 community cards
for x in range(0, 4):
    card = Poker.deck.draw()
    Poker.player.add_hand(card)
    card = Poker.deck.draw()
    Poker.community_cards.append(card)

Poker.player.show_hand()

#return cards and get new cards
returned_cards = Poker.player.return_cards()

for x in range(0, returned_cards):
    card = Poker.deck.draw()
    Poker.player.add_hand(card)

#second bet
print("Make your bet")

debug = True
while debug == True:
    second_bet = input()
    try:
        second_bet = float(second_bet)
        debug = False
    except:
        print("invalid input")

Poker.player.bet_money(second_bet)
Poker.pot += second_bet

player_value = Poker.hand_value(Poker.player.hand)