import random

# initialize some useful global variables
in_play = False

score = 0
player = []
dealer = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

# define hand class
class Hand:
    def __init__(self):
        self.cardlist = []

    def __str__(self):
        out = ''
        n = 0
        while n in range(len(self.cardlist)):
            out += str(self.cardlist[n]) + " "
            n += 1
        return(out)

    def add_card(self, card):
        self.cardlist.append(card)

    def get_value(self):
        n = 0
        value = 0
        a = False
        while n in range(len(self.cardlist)):
            rank = self.cardlist[n].get_rank()
            value += VALUES.get(rank)
            if rank == 'A':
                a = True
                
            n += 1
        if a:
            if value + 10 <= 21:
                value += 10
        return value
        
# define deck class 
class Deck:
    def __init__(self):
        self.cardlist = []
        for s in SUITS:
            for r in RANKS:
                card = Card(s, r)
                self.cardlist.append(card)
        
    def shuffle(self):
        random.shuffle(self.cardlist)
        
    def deal_card(self):
        a = self.cardlist[-1]
        self.cardlist.pop()
        return(a)
    
    def __str__(self):
        out = ''
        n = 0
        while n in range(len(self.cardlist)):
            out += str(self.cardlist[n]) + " "
            n += 1
        return(out)


#define event handlers for buttons
def deal():
    global outcome, in_play, player, deck, dealer, score
    in_play = True
    outcome = 'Hit or Stand?'
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    c = deck.deal_card()
    player.add_card(c)
    
    dealer = Hand()
    c = deck.deal_card()
    dealer.add_card(c)
    
    c = deck.deal_card()
    player.add_card(c)

    c = deck.deal_card()
    dealer.add_card(c)
    
    print player
    ask(input("Hit or Stand?" + " (Your hand: " + str(player) + ")"))

    
def hit():
    global in_play, player, outcome, score
    # if the hand is in play, hit the player
    if in_play:
        v1 = player.get_value()
        if v1 <= 21:
            c = deck.deal_card()
            player.add_card(c)
            v1 = player.get_value()
            print player, v1
            if v1 > 21:
                in_play = False
                outcome = "You Have Busted! New Deal?"
                if input("New Deal? (yes or no)").lower() == "yes":
                    deal()                
            else:
                    ask(input("Hit or Stand?" + " (Your hand: " + str(player) + " " + str(v1) + ")"))
            print outcome
        
def stand():
    global in_play, outcome, score, dealer
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        v1 = dealer.get_value()
        v2 = player.get_value()
        while v1 <= 17:
            c = deck.deal_card()
            dealer.add_card(c)
            v1 = dealer.get_value()   
        if v1 > 21:
            if input("Dealer Bust! New Deal? (yes or no)").lower() == "yes":
                deal()
            in_play = False
        elif v1 < v2:
            if input("You Win! New Deal? (yes or no)").lower() == "yes":
                deal()            
            in_play = False
        elif (v1 <= 21 and v1 >= v2) or 21 < v2:
            if input("You Win! New Deal? (yes or no)").lower() == "yes":
                deal()            
            in_play = False
  
def ask(string):
    string = string.lower()
    if string == "hit":
        hit()
    elif string == "stand":
        stand()
            
deal()
