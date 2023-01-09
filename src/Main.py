from src.DataLoader import game_results
from src.Deck import Deck
from src.Hand import Hand
from src.Controller import *

game_on = True
player_bet = 0
# Player balance at the beginning of the game
player_balance = 500
print_player_balance(player_balance)

while game_on:
    in_round = False
    game_status = ""
    first_round = True
    surrendered = False

    # Start Game
    yes_no_answer = get_player_yes_no()
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

        # Create a deck of cards, and shuffle it.
        my_deck = Deck()
        my_deck.shuffle_deck()

        # Deal two cards each, between player and dealer.
        player_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card(-2))
        dealer_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card())

        while in_round:
            print_current_hands(player_hand, dealer_hand)

            game_status = check_game_status(player_hand, dealer_hand)

            if game_status not in game_results and player_hand.total_sum != 21:
                player_move = get_player_move()

                if player_move == "Hit":
                    player_hand.add_card(my_deck.deal_one_card())

                elif player_move == "Stand":
                    # dealer playing now
                    print("\n***** Dealer reveals his cards *****")
                    print_hands_with_dealer(player_hand, dealer_hand)
                    in_round = False

                elif player_move == "Double down":
                    if first_round:
                        new_player_bet = double_bet(player_balance, player_bet)

                        if new_player_bet > player_bet:
                            player_bet = new_player_bet
                            player_hand.add_card((my_deck.deal_one_card()))
                            print_current_hands(player_hand, dealer_hand)
                            in_round = False

                    else:
                        print("Sorry you can't double down now.")

                elif player_move == "Split":
                    print("Option is not available yet")

                elif player_move == "Surrender":
                    if first_round:
                        surrendered = True
                        game_status = "Bust"
                        in_round = False
                    else:
                        print("Sorry you can't surrender now.")

            else:
                # if game status is not "" meaning the player has lost.
                # and there's no need to let the player play more rounds nor the dealer.
                in_round = False

            if not in_round:
                # check for winner
                if game_status == "":
                    # dealer plays and results are calculated.
                    while dealer_hand.total_sum < player_hand.total_sum and dealer_hand.total_sum < 17:
                        # for card in my_deck.all_cards:
                        #     print(card)
                        dealer_hand.add_card(my_deck.deal_one_card())
                        print_hands_with_dealer(player_hand, dealer_hand)

                    game_status = check_game_status(player_hand, dealer_hand, True)

                if game_status == "Win":
                    print("Congratulations")
                    player_balance = win_money(player_balance, player_bet)
                elif game_status == "Bust":
                    if surrendered:
                        print("Player surrendered!!")
                        player_bet = int(player_bet/2)
                        player_balance = lose_money(player_balance, player_bet)
                    else:
                        print("Oh oh! You lost!!")
                        player_balance = lose_money(player_balance, player_bet)
                elif game_status == "Push":
                    print("Push!! \nGame over\n")
                    # nothing happens to money game ends
                else:
                    print("Error!")

            first_round = False

        print_player_balance(player_balance)
