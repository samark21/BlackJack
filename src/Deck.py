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

    def deal_one_card(self):
        '''
        deals the top (last) card from the deck
        :return: Card
        '''
        return self.all_cards.pop()