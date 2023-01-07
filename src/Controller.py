from src.DataLoader import player_yes_no, player_options


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
    player_balance += amount
    return player_balance


def lose_money(player_balance, amount):
    player_balance -= amount


def user_round_option():
    option = input("What's your move? ")


def get_user_yes_no():
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
    if balance >= bet:
        return True
    else:
        return False
