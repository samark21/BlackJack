class Hand:

    def __init__(self, card1, card2):
        self.current_hand = []
        self.current_hand.append(card1)
        self.current_hand.append(card2)
        self.cards_string = ""
        self.total_sum = 0

    def add_card(self, added_card):
        self.current_hand.append(added_card)

    def total_value(self):
        self.total_sum = 0
        for card in self.current_hand:
            self.total_sum += card.value
        if self.total_sum > 21:
            for card in self.current_hand:
                if card.rank == "Ace":
                    self.total_sum -= 10
        return self.total_sum

    def __str__(self):
        self.cards_string = ""
        for card in self.current_hand:
            self.cards_string += str(card) + " | "

        return f"Hand: {self.cards_string} Total: {self.total_sum}"
