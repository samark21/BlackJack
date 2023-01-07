from src.Deck import Deck
from src.Hand import Hand
from src.Controller import *

game_on = True
player_bet = 0
# Player balance at the beginning of the game
player_balance = 500
print_player_balance(player_balance)

# Create a deck of cards, and shuffle it.
my_deck = Deck()
my_deck.shuffle_deck()

# # Deal two cards each, between player and dealer.
# player_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card(-2))
# dealer_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card())
#
# print_current_hands(player_hand, dealer_hand)


while game_on:
    in_round = False
    # Start Game
    yes_no_answer = get_user_yes_no()
    if not yes_no_answer:
        # Player doesn't want to play
        game_on = False
        break

    elif player_balance <= 0:
        print("You don't have money!!\nWe're going to have to ask you to leave the table!")
        game_on = False
        break

    elif yes_no_answer:
        player_bet = set_bet(player_balance)
        in_round = True
        # Deal two cards each, between player and dealer.
        player_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card(-2))
        dealer_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card())

        while in_round:


            print_current_hands(player_hand, dealer_hand)

            # player_move =
            in_round = False



    game_on = False
