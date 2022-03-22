from pypoker import Poker
import time
poker = Poker('plo5', 6)
num_iterations = 1000
t = 0

for i in range(num_iterations):
    t1 = time.time()
    cards = poker.deal()
    winner = poker.declare_winner(
        player_cards=cards['player_cards'],
        community_cards=cards['community_cards']
    )
    t2 = time.time()
    t += t2 - t1

print("Total time taken for {} iterations: {:.2f} s".format(num_iterations, t))
