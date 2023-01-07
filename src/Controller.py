from src.DataLoader import player_yes_no, player_moves, game_results


def print_current_hands(p_hand, d_hand):
    print("\n_____________________________________________________________")
    print(f"Player {p_hand}")
    print(f"Dealer Hand: *Face Down* | {d_hand.current_hand[1]} | Value: {d_hand.current_hand[1].value}")
    print("_____________________________________________________________\n")


def print_hands_with_dealer(p_hand, d_hand):
    print("\n_____________________________________________________________")
    print(f"Player {p_hand}")
    print(f"Dealer {d_hand}")
    print("_____________________________________________________________\n")


def print_player_balance(balance):
    print("**********************")
    print(f"Player Balance: ${balance}")
    print("**********************")


def win_money(player_balance, amount):
    """
    In case the player wins, add the amount of money to their current balance.
    :param player_balance: current player balance
    :param amount: value of bet placed. The player wins the same amount as their bet (not 3:2)
    :return: player's updated balance.
    """
    player_balance += amount
    return player_balance


def lose_money(player_balance, amount):
    """
    In case the player loses, subtract the amount of money from their current balance
    :param player_balance: player's current balance
    :param amount: value of the bet the player placed.
    :return: player's updated balance
    """
    player_balance -= amount
    return player_balance


def get_player_move():
    print("Your options are:")
    print("* Hit")
    print("* Stand")
    print("* Double down")
    print("* Split")
    print("* Surrender\n")

    option = input("What's your move? ")
    while option.casefold().capitalize() not in player_moves:
        print("Wrong input please try again")
        option = input("What's your move? ")

    if option.casefold().capitalize() in player_moves:
        return option.casefold().capitalize()


def get_player_yes_no():
    """
    Get the player's answer to whether they want to play or not.
    checks if there's a problem with them joining the table.
    and in case they want to quit this allows them to do so.
    :return: boolean: True - play, False - quit.
    """
    option = input("Do you want to play? ")

    while option.casefold().capitalize() not in player_yes_no:
        print("Wrong input please enter Yes/No only.")
        option = input("Do you want to play? ")

    if option.casefold().capitalize() in player_yes_no:
        if option.casefold().capitalize() == "Yes":
            return True
        else:
            return False


def set_bet(balance):
    """
    takes an input from the player to set as a bet.
    calls check_bet() to check if the player can set such bet (if they have the said amount of money)
    :param balance: current player's balance
    :return: the set bet
    """
    bet = input("Place your bet: ")

    while not bet.isnumeric() or bet == "0":
        print("Wrong input please enter a natural number only")
        bet = input("Place your bet: ")

    else:
        valid = check_bet(balance, int(bet))
        if valid:
            return int(bet)
        else:
            print("Sorry you don't have that much money!\nPlease set a smaller bet.")
            set_bet(balance)


def check_bet(balance, bet):
    """
    check if the player can set such bet (if they have the said amount of money)
    :param balance: current player balance
    :param bet: amount of money they want to bet on
    :return: boolean, True - they can set such bet, False - they cannot bet this amount of money.
    """
    if balance >= bet:
        return True
    else:
        return False


def check_game_status(player_h, dealer_h, dealer_turn=False):
    game_status = ""
    if not dealer_turn:
        if player_h.total_sum == 21 and dealer_h.total_sum == 21:
            game_status = "Push"
        elif dealer_h.total_sum == 21:
            game_status = "Bust"

    else:
        if player_h.total_sum == 21 and dealer_h.total_sum == 21:
            game_status = "Push"
        elif dealer_h.total_sum == 21:
            game_status = "Bust"
        elif player_h == 21:
            game_status = "Win"
        elif player_h > 21:
            game_status = "Bust"
        elif player_h < 21:
            if player_h == dealer_h:
                game_status = "Push"
            elif player_h < dealer_h < 21:
                game_status = "Bust"
            elif dealer_h > 21:
                game_status = "Win"
            elif dealer_h < player_h < 21:
                game_status = "Win"

    return game_status
