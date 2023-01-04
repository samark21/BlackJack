from src.DataLoader import get_values

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = get_values(rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

