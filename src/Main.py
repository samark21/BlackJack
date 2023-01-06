from src.Deck import Deck
from src.Hand import Hand

my_deck = Deck()
my_deck.shuffle_deck()
# for i in range(0, 52):
#     print(my_deck.all_cards[i])
player_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card(-2))
dealer_hand = Hand(my_deck.deal_one_card(), my_deck.deal_one_card())
print("_____________________________________________________________")

print(f"Player {player_hand}")
print("Player " + str(player_hand.total_value()))

print(f"Dealer {dealer_hand}")
print("Dealer " + str(dealer_hand.total_value()))

player_hand.add_card(my_deck.deal_one_card())
player_hand.add_card(my_deck.deal_one_card())
dealer_hand.add_card(my_deck.deal_one_card())
dealer_hand.add_card(my_deck.deal_one_card())

print(f"Player {player_hand}")
print("Player " + str(player_hand.total_value()))

print(f"Dealer {dealer_hand}")
print("Dealer " + str(dealer_hand.total_value()))



