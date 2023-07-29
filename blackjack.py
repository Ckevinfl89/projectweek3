import random
import os

def clear_output():
    os.system("cls" if os.name == "nt" else "clear")

suits = ("♥", "♦", "♣", "♠")
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10, 'Q': 10, 'A': 11}

class Card:
    
    def __init__(self, suit, card_title):
        self.suit = suit
        self.card_title = card_title
        self.card_value = card_values[card_title]

    def __repr__(self):
        return f"<{self.card_title} of {self.suit}"

    def show(self):
        print('┌───────┐')
        print(f'| {self.card_title:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.card_title:>2} |')
        print('└───────┘')

class Game:
    def __init__(self):
        self.deck = []
        self.shuffle()
        self.dealer = Player('bobert')
        self.player = Player('kevin')

    def shuffle(self):
        self.deck = []
        for suit in suits:
            for card_value in card_values:
                self.deck.append(Card(suit, card_value))
        random.shuffle(self.deck)

    def deal(self):
        for i in range(2):
            dealt_card = self.deck.pop()
            self.player.hand.append(dealt_card)
            self.player.value += dealt_card.card_value
            if dealt_card.card_title == 'A':
                self.player.aces += 1

            dealt_card = self.deck.pop()
            self.dealer.hand.append(dealt_card)
            self.dealer.value += dealt_card.card_value
            if dealt_card.card_title == 'A':
                self.dealer.aces += 1

    def adjust_for_ace(self, player):
        while player.value > 21 and player.aces:
            player.value -= 10
            player.aces -= 1

    def hit(self, player):
        card = self.deck.pop()
        player.hand.append(card)
        player.value += card.card_value
        if card.card_title == 'A':
            player.aces += 1
        self.adjust_for_ace(player)

    def stand(self):
        while self.dealer.value < 17:
            self.hit(self.dealer)

    def display(self):
        print(f"Player has: {self.player.value}")
        for card in self.player.hand:
            card.show()

        print(f"Dealer has: {self.dealer.value}")
        for card in self.dealer.hand:
            card.show()

    def action(self):
        print("\nHi friend! It's time to play!")
        while True:
            response = input("Would you like to: Hit, or Stand? ").lower()
            if response == 'hit':
                clear_output()
                self.hit(self.player)
                self.display()
                if self.player.value > 21:
                    print("Bust! You lose.")
                    break
            elif response == 'stand':
                clear_output()
                self.stand()
                self.display()
                if self.dealer.value > 21 or self.player.value > self.dealer.value:
                    print("You win!")
                elif self.dealer.value == self.player.value:
                    print("You lose!")
                else:
                    print("You lose!")
                break
            else:
                print(f"'{response.title()}' is not one of the available options. Please select 'hit' or 'stand'.")

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0
        self.aces = 0

game = Game()
game.shuffle()
game.deal()
game.display()
game.action()
