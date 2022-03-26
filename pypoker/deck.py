import random


class Deck(object):
    """
    Emulates a deck of cards
    """

    def __init__(self, num_decks=1) -> None:
        """
        Initialize the deck
        """
        self.num_decks = num_decks
        self.deck = {
            "2s": self.num_decks,
            "3s": self.num_decks,
            "4s": self.num_decks,
            "5s": self.num_decks,
            "6s": self.num_decks,
            "7s": self.num_decks,
            "8s": self.num_decks,
            "9s": self.num_decks,
            "Ts": self.num_decks,
            "Js": self.num_decks,
            "Qs": self.num_decks,
            "Ks": self.num_decks,
            "As": self.num_decks,
            "2c": self.num_decks,
            "3c": self.num_decks,
            "4c": self.num_decks,
            "5c": self.num_decks,
            "6c": self.num_decks,
            "7c": self.num_decks,
            "8c": self.num_decks,
            "9c": self.num_decks,
            "Tc": self.num_decks,
            "Jc": self.num_decks,
            "Qc": self.num_decks,
            "Kc": self.num_decks,
            "Ac": self.num_decks,
            "2d": self.num_decks,
            "3d": self.num_decks,
            "4d": self.num_decks,
            "5d": self.num_decks,
            "6d": self.num_decks,
            "7d": self.num_decks,
            "8d": self.num_decks,
            "9d": self.num_decks,
            "Td": self.num_decks,
            "Jd": self.num_decks,
            "Qd": self.num_decks,
            "Kd": self.num_decks,
            "Ad": self.num_decks,
            "2h": self.num_decks,
            "3h": self.num_decks,
            "4h": self.num_decks,
            "5h": self.num_decks,
            "6h": self.num_decks,
            "7h": self.num_decks,
            "8h": self.num_decks,
            "9h": self.num_decks,
            "Th": self.num_decks,
            "Jh": self.num_decks,
            "Qh": self.num_decks,
            "Kh": self.num_decks,
            "Ah": self.num_decks,
        }

    def get_unique_card_sets(self, num_sets: int, set_length: int, output_format: str = 'str', deck: dict = None) -> list:
        """
        Get a list of unique card sets
        """
        if deck is not None:
            self.deck = deck
        if num_sets * set_length > sum(self.deck.values()):
            raise ValueError("Not enough cards in the deck.")
        cards = []
        for card, times in self.deck.items():
            for _ in range(times):
                cards.append(card)
        sample = random.sample(cards, num_sets * set_length)

        for s in sample:
            self.deck[s] -= 1

        if output_format == 'str':
            return [
                ''.join(sample[i:i + set_length])
                for i in range(0, len(sample), set_length)
            ]
        elif output_format == 'list':
            return [
                sample[i:i + set_length]
                for i in range(0, len(sample), set_length)
            ]
        else:
            raise ValueError("Invalid output format.")

    # def get_random_cards(self, n) -> list:

    def get_community_cards(self) -> list:
        """
        Get a list of community cards
        """
        remaining_deck = {
            k: v
            for k, v in self.deck.items()
            if v > 0
        }
        return self.get_unique_card_sets(1, 5, output_format='list', deck=remaining_deck)[0]

    def deal_poker_hands(self, game_variant: str, num_players: int) -> dict:
        """
        Return a dictionary of poker hands based on game type

        Dictionary contains the following key-value pairs:

            'community_cards': list of community cards

            'player_cards': dictionary of player cards

            'variant': game variant

            'flop': string of flop cards

            'turn': string of turn card

            'river': string of river card
        """
        if game_variant == 'nlh':
            player_cards = self.get_unique_card_sets(num_players, 2)
        elif game_variant == 'plo4':
            player_cards = self.get_unique_card_sets(num_players, 4)
        elif game_variant == 'plo5':
            player_cards = self.get_unique_card_sets(num_players, 5)
        elif game_variant == 'plo6':
            player_cards = self.get_unique_card_sets(num_players, 6)
        community_cards = self.get_community_cards()
        dic = {
            'variant': game_variant,
            'player_cards': {
                'p{}'.format(i+1): player_cards[i] for i in range(num_players)
            },
            'flop': community_cards[0] + community_cards[1] + community_cards[2],
            'turn': community_cards[3],
            'river': community_cards[4],
            'community_cards': "".join(community_cards)
        }
        self.reset_deck()
        return dic

    def reset_deck(self):
        """
        Reset the deck to the full count
        """
        self.deck = {
            "2s": self.num_decks,
            "3s": self.num_decks,
            "4s": self.num_decks,
            "5s": self.num_decks,
            "6s": self.num_decks,
            "7s": self.num_decks,
            "8s": self.num_decks,
            "9s": self.num_decks,
            "Ts": self.num_decks,
            "Js": self.num_decks,
            "Qs": self.num_decks,
            "Ks": self.num_decks,
            "As": self.num_decks,
            "2c": self.num_decks,
            "3c": self.num_decks,
            "4c": self.num_decks,
            "5c": self.num_decks,
            "6c": self.num_decks,
            "7c": self.num_decks,
            "8c": self.num_decks,
            "9c": self.num_decks,
            "Tc": self.num_decks,
            "Jc": self.num_decks,
            "Qc": self.num_decks,
            "Kc": self.num_decks,
            "Ac": self.num_decks,
            "2d": self.num_decks,
            "3d": self.num_decks,
            "4d": self.num_decks,
            "5d": self.num_decks,
            "6d": self.num_decks,
            "7d": self.num_decks,
            "8d": self.num_decks,
            "9d": self.num_decks,
            "Td": self.num_decks,
            "Jd": self.num_decks,
            "Qd": self.num_decks,
            "Kd": self.num_decks,
            "Ad": self.num_decks,
            "2h": self.num_decks,
            "3h": self.num_decks,
            "4h": self.num_decks,
            "5h": self.num_decks,
            "6h": self.num_decks,
            "7h": self.num_decks,
            "8h": self.num_decks,
            "9h": self.num_decks,
            "Th": self.num_decks,
            "Jh": self.num_decks,
            "Qh": self.num_decks,
            "Kh": self.num_decks,
            "Ah": self.num_decks,
        }

    def knock_cards(self, list_of_cards):
        """
        Remove cards from the deck
        """
        for card in list_of_cards:
            self.deck[card] -= 1

    def get_random_cards(self, num_cards) -> str:
        """
        Get random cards
        """
        remaining_deck = []
        for card, times in self.deck.items():
            for _ in range(times):
                remaining_deck.append(card)
        return random.sample(remaining_deck, num_cards)
        pass

    def knockout_cards(self, deadcards: str):
        """
        Update the dead cards
        """
        if not deadcards or not len(deadcards):
            return None
        if isinstance(deadcards, str):
            deadcards = [deadcards[i: i+2]
                         for i in range(0, len(deadcards), 2)]
        for card in deadcards:
            self.deck[card] -= 1


if __name__ == '__main__':
    deck = Deck()
    print(deck.get_unique_card_sets(5, 5, 'str'))
    print(deck.deal_poker_hands('plo5', 3))
