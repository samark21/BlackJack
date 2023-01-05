import random

from src import DataLoader
from src.Card import Card


class Deck:

    def __init__(self):
        # holding the cards (the deck) in a list
        self.all_cards = []

        for suit in DataLoader.suits:
            for rank in DataLoader.ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        '''
        shuffles the deck of cards randomly
        :return: --
        '''
        random.shuffle(self.all_cards)

    def deal_one_card(self, x=-1):
        '''
        deals the top (last) card from the deck by default
        but when giving out cards, the dealer must pass the cards in a "circle" around the players (including himself)
        thus, passing the location of the card to pop will be useful when dealing the hands in the beginning.
        :return: Card
        '''
        return self.all_cards.pop(x)
