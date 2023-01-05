class Hand:
    current_hand = []

    def __init__(self, card1, card2):
        self.current_hand.append(card1)
        self.current_hand.append(card2)

    def add_card(self, added_card):
        self.current_hand.append(added_card)
