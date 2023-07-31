import random
from random import choice
from time import sleep

# ----------------------------------------------------------
# Create a deck of 52 cards 
# Shuffle the deck
# Ask the Player for their bet
# Make sure that the Player’s bet does not exceed their available chips
# Deal two cards to the Dealer and two cards to the Player
# Show only one of the Dealer’s cards, the other remains hidden
# Show both of the Player’s cards
# Ask the Player if they wish to Hit, and take another card
# If the Player’s hand doesn’t Bust (go over 21) , ask if they’d like to Hit again
# If a Player Stands, play the Dealer’s hand. The dealer will always Hit until the Dealer’s value meets or exceeds 17
# Determine the winner and adjust the Player’s chips accordingly
# Ask the Player if they’d like to play again
# ----------------------------------------------------------
# determine suits or just numbers?

# Create a card Class
suits = ('♥','♦','♣', '♠')
card_types= ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A')
card_values = {'2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'K':10, 'Q':10, 'A':11}

class Card:
    def __init__(self, suit, card_value):
        self.suit = suit
        self.card_value = card_value
       
    def __repr__(self):
        return f"<{self.card_value} of {self.suit}"
    
    # def show(self):
    #     print('┌───────┐')
    #     print(f'| {self.card_value:<2}    |')
    #     print('|       |')
    #     print(f'|   {self.suit}   |')
    #     print('|       |')
    #     print(f'|    {self.card_value:>2} |')
    #     print('└───────┘')
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for card_type in card_types:
                self.deck.append(Card(suit, card_type))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
        

# class Deck:


    # def shuffle(self):
    #     self.deck = []
    #     for suit in suits:
    #         for card_value in card_values:
    #             self.deck.append(Card(suit, card_value))
    #     random.shuffle(self.deck)

    
    # def deal(self):
    #     for i in range(2):
    #         dealt_card = self.deck.pop()
    #         self.player.hand.append(dealt_card)
    #         dealt_card = self.deck.pop()
    # #         self.dealer.hand.append(dealt_card)

    # def display(self):
    #     print("Player has ")
    #     for card in self.player.hand:
    #         card.show()

    #     print("Dealer has ")
    #     for card in self.dealer.hand:
    #         card.show()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card_values[card.card_type]
        if card.card_type == 'A':
            self.aces += 1

    def adjust_for_a(self):
        while self.value > 21 and self.a:
            self.value -= 10
            self.aces -= 1
    
class Chips:
    def __init__(self):
        self.total = 100

        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Bet must be a number amount')
        else:
            if chips.bet > chips.total:
                print("You bet cannot exceed", chips.total)
            else:
                break

def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x= input("Would you like to Hit or Stand? Enter 'h' or 's' ").lower()

        if x[0].lower()== 'h':
            hit(deck, hand)

        elif x[0].lower == 's':
            print("Player stands. Dealer is playing")
            playing = False

        else:
            print(":( please try again")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<car hidden>")
    print('', dealer.cards[1])
    print("\n Player's Hand =", *player.cards, sep='\n')
    
def show_all(player, dealer):
    print("\nDealer hand:", *dealer.cards, sep='\n ' )
    print("Dealer's hand =", dealer.card_value)
    print("\nPlayer's hand:", *player.cards, sep='\n ')
    print("Player's hand=", player.card_value)

def player_burst(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer burst!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet

def push(player, dealer):
    print("Is a Tie")

while True:

    print("Welcome to blackjack")

    deck= Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

    if player_hand.value >21:
        player_burst(player_hand, dealer_hand, player_chips)
        break


if player_hand.value <= 21:

    while dealer_hand.value < 17:
        hit(deck, dealer_hand)

    show_all(player_hand,dealer_hand)

    if dealer_hand.value > 21:
        dealer_busts(player_hand, dealer_hand, player_chips)

    elif dealer_hand.value > player_hand.value:
        player_wins(player_hand, dealer_hand, player_chips.total)

    new_game = input("Enter 'y' to play or 'no' to quit  ")

    if new_game[0].lower()=='y':
        playing=True
        
    else:
        print("Thanks for playing")
        




    


# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.hand = []

# game = Game()
# game.deal()
# game.display()


# Create a deck
# Create 'shuffle' which would be a random from import
# Create a hand for dealer and for player
# Betting option, $$ or chips, (I like chips if we can)
# Take a bet