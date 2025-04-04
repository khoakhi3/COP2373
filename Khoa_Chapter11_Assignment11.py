#Khoa Duong
#Assignmetn 11
#Write a program that deal 5 card then ask user to pick the cards to be replace.

import random
#Write out the card and suits.
class Card:
    suit_names = ['Spade', 'Club', 'Diamond', 'Heart']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8'
                  , '9', '10', 'Jack', 'Queen', 'King']
#Set up card.
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
#Make the print readable.
    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

#Create a full deck.
class Deck:
#shuffle the deck.
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range (1,14)]
        random.shuffle(self.cards)
#return the top card.
    def draw(self):
        return self.cards.pop()

#Deal the card.
def deal_card(deck):
    hand = [deck.draw() for _ in range(5)]
#Print out the hand.
    print('Your hand:')
    for i, card in enumerate(hand, 1):
        print(f'{i}. {card}')
    return hand
        
#Ask user to switch cards and display the result.
def main():
    deck = Deck()
    hand = deal_card(deck)
#Ask user to replace cards they wanted.
    response = input('Enter card number to be replace (ex: 1,3) or press enter to keep all: ')
#convert user's input into list of indexes.
    if response.strip():
        #Replace all cards.
        if response.strip().lower() == 'all':
            hand = [deck.draw() for _ in range(5)]
        else:
            try:
                indexes = [int(num.strip()) - 1 for num in response.split(',')]
                for i in indexes:
                    #Replace desired cards.
                    if 0 <= i < 5:
                        hand[i] = deck.draw()
            except ValueError:
                print('Invalid input!! no card replaced.')
    #Show the final hand.
    print('Your final hand:')
    for i, card in enumerate(hand, 1):
        print(f'{i}. {card}')

main()
