from .deck import Deck
from .evaluator import Evaluator
from .misc import fuzzy_match_game_name

class Poker(object):

    def __init__(self, game_type, num_players, num_decks=1):
        self.deck = Deck(num_decks)
        self.evaluator = Evaluator()
        self.game_type = fuzzy_match_game_name(game_type)
        self.num_players = num_players
        self.num_decks = num_decks

    def deal(self):
        """
        Deal cards to players
        """
        return self.deck.deal_poker_hands(self.game_type, self.num_players)

    def declare_winner(self, player_cards, community_cards):
        """
        Declare winner
        """
        return self.evaluator.declare_winner(
            player_cards=player_cards,
            community_cards=community_cards,
            game_type=self.game_type
        )
