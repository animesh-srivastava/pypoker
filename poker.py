from pypoker import Poker
from pprint import pprint

poker = Poker('plo6', 6)
cards = poker.deal()
winner = poker.declare_winner(
    player_cards=cards['player_cards'],
    community_cards=cards['community_cards']
)
pprint(cards)
pprint(winner)
