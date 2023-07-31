import random
import tkinter as tk
from tkinter import messagebox


suits = ('♥', '♦', '♣', '♠')
card_types = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A')
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10, 'Q': 10, 'A': 11}

# Add path to your card images here
CARD_IMAGES = {
    '♥': 'path_to_heart_image.png',
    '♦': 'path_to_diamond_image.png',
    '♣': 'path_to_club_image.png',
    '♠': 'path_to_spade_image.png'
}

class Card:
    def __init__(self, suit, card_value):
        self.suit = suit
        self.card_value = card_value

    def __repr__(self):
        return f"<{self.card_value} of {self.suit}>"

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for card_type in card_types:
                self.deck.append(Card(suit, card_type))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card_values[card.card_value]
        if card.card_value == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
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

class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

        self.dealer_hand = Hand()
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

        self.player_chips = Chips()

        self.label = tk.Label(root, text="Welcome to Blackjack", font=("Arial", 16))
        self.label.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(root, text="Stand", command=self.stand)
        self.stand_button.pack()

        self.new_game_button = tk.Button(root, text="New Game", command=self.new_game)
        self.new_game_button.pack()

        self.card_images = {}
        for suit in suits:
            for card_type in card_types:
                # card_image = Image.open(CARD_IMAGES[suit])
                # card_image = card_image.resize((50, 70), Image.ANTIALIAS)
                # self.card_images[(suit, card_type)] = ImageTk.PhotoImage(card_image)

        self.update_display()

    def update_display(self):
        player_text = f"Player's hand:\n{self.get_card_image(self.player_hand.cards[0])} {self.get_card_image(self.player_hand.cards[1])}\n\nPlayer's hand value: {self.player_hand.value}"
        dealer_text = f"Dealer's hand:\n{self.get_card_image(self.dealer_hand.cards[0])} {self.get_card_image(self.dealer_hand.cards[1])}"
        chips_text = f"Chips: {self.player_chips.total}"

        self.label.config(text=player_text + "\n\n" + dealer_text + "\n\n" + chips_text)

    def get_card_image(self, card):
        return tk.Label(self.root, image=self.card_images[(card.suit, card.card_value)])

    def hit(self):
        hit(self.deck, self.player_hand)
        self.update_display()
        if self.player_hand.value > 21:
            self.player_bust()

    def stand(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        while self.dealer_hand.value < 17:
            hit(self.deck, self.dealer_hand)
        self.update_display()
        if self.dealer_hand.value > 21 or self.dealer_hand.value < self.player_hand.value:
            self.player_wins()
        elif self.dealer_hand.value > self.player_hand.value:
            self.dealer_wins()
        else:
            self.push()

    def player_bust(self):
        messagebox.showinfo("Result", "Player busts!")
        self.player_chips.lose_bet()
        self.update_display()
        self.new_game_button.config(state=tk.NORMAL)

    def player_wins(self):
        messagebox.showinfo("Result", "Player wins!")
        self.player_chips.win_bet()
        self.update_display()
        self.new_game_button.config(state=tk.NORMAL)

    def dealer_wins(self):
        messagebox.showinfo("Result", "Dealer wins!")
        self.player_chips.lose_bet()
        self.update_display()
        self.new_game_button.config(state=tk.NORMAL)

    def push(self):
        messagebox.showinfo("Result", "It's a Tie")
        self.update_display()
        self.new_game_button.config(state=tk.NORMAL)

    def new_game(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

        self.dealer_hand = Hand()
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.new_game_button.config(state=tk.DISABLED)

        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackApp(root)
    root.mainloop()
