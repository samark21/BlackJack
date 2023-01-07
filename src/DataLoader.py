# In the mean time, the data will be set manually here
# But I plan on reading it from a file later on. for example a .txt

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

player_moves = ("Hit", "Stand", "Double down", "Split", "Surrender")

player_yes_no = ("Yes", "No")

game_results = ("Win", "Bust", "Push")  # Bust = lose, Push = tie


def get_values(rank):
    return values[rank]
