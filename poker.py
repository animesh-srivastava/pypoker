from pypoker import Poker, Simulator
from pprint import pprint

# poker = Poker('plo6', 6)
# cards = poker.deal()
# winner = poker.declare_winner(
#     player_cards=cards['player_cards'],
#     community_cards=cards['community_cards']
# )
# pprint(cards)
# pprint(winner)

simulator = Simulator('plo4')
sim_results = simulator.simulate('2s3s4s5s', '2h3h4h5h', 10000)
print(sim_results[0] * 100, sim_results[1] * 100)
sim_results[2].to_csv('sim_results.csv')
