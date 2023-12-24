import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')    
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=value[rank]
        
    def __str__(self):
        return (self.suit+" - "+self.rank)
    
class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''  
        for card in self.deck:
            deck_comp += '\n '+card.__str__() 
        return ('The deck has:' + deck_comp)
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Player:
    
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
        
    def __str__(self):
        return self.name+'has'+len(self.cards)+'cards'
    
    def playcard(self):
        p=self.cards.pop(0)
        self.value-=p.value
        return p
        
    def addcard(self,card):
        if type(card)==type([]):
            self.cards.extend(card)
            for i in card:
                self.value+=i.value
                if i.rank=='Ace':
                    self.aces+=1
        else:
            self.cards.append(card)
            self.value+=card.value
            if card.rank=='Ace':
                    self.aces+=1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces>0:
            self.value -= 10
            self.aces -= 1  

class Chips:
    
    def __init__(self):
        self.total=100
        self.bet=0
            
    def winbet(self):
        self.total+=self.bet
        
    def losebet(self):
        self.total-=self.bet
        
        
def bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break


def hit(deck,player):
    player.addcard(deck.deal())
    player.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
    
def hidden(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def visible(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
    
def playerwins(player,dealer,chips):
    print("Player wins!")
    chips.winbet()

def dealerbusts(player,dealer,chips):
    print("Dealer busts!")
    chips.winbet()
    
def dealerwins(player,dealer,chips):
    print("Dealer wins!")
    chips.losebet()
    
def playerbusts(player,dealer,chips):
    print("Player busts!")
    chips.losebet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")



playing = True
 # Print an opening statement
print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until he reaches 17.\nAces count as 1 or 11.')
player_chips = Chips() 
while True:
     
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player = Player()
    player.addcard(deck.deal())
    player.addcard(deck.deal())
    
    dealer = Player()
    dealer.addcard(deck.deal())
    dealer.addcard(deck.deal())
            
    
    # Prompt the Player for their bet
    bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    hidden(player,dealer)
    
    while playing: 
        
        hit_or_stand(deck,player) 
        
        # Show cards (but keep one dealer card hidden)
        hidden(player,dealer)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            playerbusts(player,dealer,player_chips)
            break     

    print("_"*30)

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player.value <= 21:
        
        while dealer.value < 17:
            hit(deck,dealer)    
    
        # Show all cards
        visible(player,dealer)
        
        if dealer.value > 21:
            dealerbusts(player,dealer,player_chips)

        elif dealer.value > player.value:
            dealerwins(player,dealer,player_chips)

        elif dealer.value < player.value:
            playerwins(player,dealer,player_chips)

        else:
            push(player,dealer)        
    
    print("\nPlayer's winnings stand at",player_chips.total)
    print()
    
    new_game = input("Would you like to play another Game? Enter 'Y' or 'N' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("\nThanks for playing!")
        print(f"\nYour winnings are : {player_chips.total}")
        break
