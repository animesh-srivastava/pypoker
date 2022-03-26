from itertools import combinations


class Evaluator(object):

    def __init__(self):
        """
        Initialize the class
        """
        self.card_strengths = {
            1: "Royal Flush",
            2: "Straight Flush",
            3: "Four of a Kind",
            4: "Full House",
            5: "Flush",
            6: "Straight",
            7: "Three of a Kind",
            8: "Two Pair",
            9: "One Pair",
            10: "High Card"
        }
        self.suites = ["s", "h", "d", "c"]
        self.ranks = ["2", "3", "4", "5", "6",
                      "7", "8", "9", "T", "J", "Q", "K", "A"]
        self.rank_and_suites = [
            "As", "Ad", "Ac", "Ah",
            "Ks", "Kd", "Kc", "Kh",
            "Qs", "Qd", "Qc", "Qh",
            "Js", "Jd", "Jc", "Jh",
            "Ts", "Td", "Tc", "Th",
            "9s", "9d", "9c", "9h",
            "8s", "8d", "8c", "8h",
            "7s", "7d", "7c", "7h",
            "6s", "6d", "6c", "6h",
            "5s", "5d", "5c", "5h",
            "4s", "4d", "4c", "4h",
            "3s", "3d", "3c", "3h",
            "2s", "2d", "2c", "2h"
        ]

    def _is_royal_flush(self, cards: list) -> tuple:
        """
        Check if the cards are a royal flush
        Returns a tuple with 3 values:
        1. True if the cards are a royal flush
        2. The index of the highest card
        3. The highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        is_flush = self._is_flush(cards)
        is_straight = self._is_straight(cards)
        is_royal = self._is_royal(cards)
        if is_flush[0] and is_royal[0] and is_straight[0]:
            return True, is_straight[1], is_straight[2]
        return False, -1, None

    def _is_straight_flush(self, cards: list) -> bool:
        """
        Check if the cards are a straight flush
        Returns a tuple with 3 values:
        1. True if the cards are a straight flush
        2. The index of the highest card
        3. The highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        is_flush = self._is_flush(cards)
        is_straight = self._is_straight(cards)
        if is_flush[0] and is_straight[0]:
            return True, is_straight[1], is_straight[2]
        return False, -1, None

    def _is_royal(self, cards: list) -> tuple:
        """
        Check if the highest card is Ace
        Returns a tuple of 3 values:
        1. True if the highest card is an Ace
        2. The index of the Ace
        3. The Ace
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        ranks = [card[0] for card in cards]
        ranks = sorted(ranks, key=lambda x: self.ranks.index(x))
        if ranks[-1] == 'A':
            return True, self.ranks.index(ranks[-1]), ranks[-1]
        return False, -1, None

    def _is_flush(self, cards: list) -> tuple:
        """
        Check if the cards are a flush
        Returns a tuple with 3 values:
        1. True if the cards are a flush
        2. The index of the highest card
        3. The highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        suites = [card[1] for card in cards]
        if len(set(suites)) == 1:
            sorted_ranks = sorted(
                cards, key=lambda x: self.ranks.index(x[0]))[-1][0]
            return True, self.ranks.index(sorted_ranks[-1]), sorted_ranks[-1]
        return False,  -1, None

    def _is_straight(self, cards: list) -> tuple:
        """
        Check if the cards form a straight
        Returns a tuple with 3 values:
        1. True if the cards form a straight
        2. The index of the highest card
        3. The highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        ranks = [card[0] for card in cards]
        ranks = sorted(ranks, key=lambda x: self.ranks.index(x))
        if ranks[-1] == "A":
            if all([i in ranks for i in ["2", "3", "4", "5"]]):
                return True, self.ranks.index("5"), "5"
            elif all([i in ranks for i in ["T", "J", "Q", "K"]]):
                return True, self.ranks.index("A"), "A"
            else:
                return False, -1, None
        else:
            start = self.ranks.index(ranks[0]) + 1
            for i in range(start, start + 5):
                if self.ranks[i] not in ranks:
                    return False, -1, None
            return True, self.ranks.index(ranks[-1]), ranks[-1]

    def _is_four_of_a_kind(self, cards: list) -> tuple:
        """
        Check if the cards are four of a kind
        Returns a tuple with 3 values:
        1. True if the cards are four of a kind
        2. The index of the highest card
        3. The highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        ranks = [card[0] for card in cards]
        counts = {
            rank: ranks.count(rank)
            for rank in ranks
        }
        if 4 in counts.values():
            for rank, count in counts.items():
                if count == 4:
                    return True, self.ranks.index(rank), rank
        return False, -1, None

    def _is_full_house(self, cards: list) -> tuple:
        """
        Check if the cards are a full house
        Returns a tuple with 5 values:
        1. True if the cards are a full house
        2. The index of the highest card
        3. The highest card
        4. The index of the second highest card
        5. The second highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        list_of_ranks = list(set([card[0] for card in cards]))
        if len(list_of_ranks) == 2:
            ranks = [card[0] for card in cards]
            if ranks.count(list_of_ranks[0]) == 2 and ranks.count(list_of_ranks[1]) == 3:
                return True, self.ranks.index(list_of_ranks[1]), list_of_ranks[1], self.ranks.index(list_of_ranks[0]), list_of_ranks[0]
            elif ranks.count(list_of_ranks[0]) == 3 and ranks.count(list_of_ranks[1]) == 2:
                return True, self.ranks.index(list_of_ranks[0]), list_of_ranks[0], self.ranks.index(list_of_ranks[1]), list_of_ranks[1]
        return False, -1, None, -1, None

    def _is_three_of_a_kind(self, cards: list) -> tuple:
        """
        Check if the cards are three of a kind
        Returns a tuple of 3 values:
        1. True if the cards are three of a kind
        2. The index of the highest card
        3. The highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]

        ranks = [card[0] for card in cards]
        counts = {
            rank: ranks.count(rank)
            for rank in ranks
        }
        if 3 in counts.values():
            for rank, count in counts.items():
                if count == 3:
                    return True, self.ranks.index(rank), rank
        return False, -1, None

    def _is_two_pair(self, cards: list) -> tuple:
        """
        Check if the cards are two pair
        Returns a tuple of 5 values:
        1. True if the cards are two pair
        2. The index of the highest card
        3. The highest card
        4. The index of the second highest card
        5. The second highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]
        ranks = [card[0] for card in cards]
        counts = {
            rank: ranks.count(rank) for rank in ranks
        }
        pair_counts = sum([1 for count in counts.values() if count == 2])
        if pair_counts != 2:
            return False, -1, None, -1, None
        else:
            current_highest = -1
            current_second_highest = -1
            for rank, count in counts.items():
                if count == 2 and self.ranks.index(rank) > current_highest:
                    current_highest = self.ranks.index(rank)
                elif count == 2 and self.ranks.index(rank) > current_second_highest:
                    current_second_highest = self.ranks.index(rank)
            return True, current_highest, self.ranks[current_highest], current_second_highest, self.ranks[current_second_highest]

    def _is_one_pair(self, cards: list) -> tuple:
        """
        Check if the cards are one pair
        Returns a tuple of 3 values:
        1. True if the cards are one pair
        2. The index of the highest card
        3. The highest card
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2]
                     for i in range(0, len(cards), 2)]

        ranks = [card[0] for card in cards]
        counts = {
            rank: ranks.count(rank) for rank in ranks
        }
        current_highest = -1

        for rank, count in counts.items():
            if count == 2 and self.ranks.index(rank) > current_highest:
                current_highest = self.ranks.index(rank)
        if current_highest == -1:
            return False, -1, None
        else:
            return True, current_highest, self.ranks[current_highest]

    def card_strength_evaluator(self, cards: list) -> tuple:
        """
        Given a set of cards, evaluate their strength and return the relevant information about it.

        Returns a tuple with following items

            1. Name of the combination
            2. Rank of the combination (1 - 10)
            3. Rank of the highest card in the combination
            4. Name of the highest card in the combination
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2] for i in range(0, len(cards), 2)]
        if len(cards) != 5:
            raise ValueError("You must provide 5 cards")
        cards = sorted(
            cards, key=lambda x: self.rank_and_suites.index(x), reverse=True)

        # check for royal flush
        tup = self._is_royal_flush(cards)
        if tup[0]:
            return "Royal Flush", 10, tup[1], tup[2]

        # check for straight flush
        tup = self._is_straight_flush(cards)
        if tup[0]:
            return "Straight Flush", 9, tup[1], tup[2]

        # check for four of a kind
        tup = self._is_four_of_a_kind(cards)
        if tup[0]:
            return "Four of a Kind", 8, tup[1], tup[2]

        # check for full house
        tup = self._is_full_house(cards)
        if tup[0]:
            return "Full House", 7, tup[1], tup[2]

        # check for flush
        tup = self._is_flush(cards)
        if tup[0]:
            return "Flush", 6, tup[1], tup[2]

        # check for straight
        tup = self._is_straight(cards)
        if tup[0]:
            return "Straight", 5, tup[1], tup[2]

        # check for three of a kind
        tup = self._is_three_of_a_kind(cards)
        if tup[0]:
            return "Three of a Kind", 4, tup[1], tup[2]

        # check for two pair
        tup = self._is_two_pair(cards)
        if tup[0]:
            return "Two Pair", 3, tup[1], tup[2]

        # check for one pair
        tup = self._is_one_pair(cards)
        if tup[0]:
            return "One Pair", 2, tup[1], tup[2]

        return "High Card", 1, self.ranks.index(cards[-1][0]), cards[-1][0]

    def get_possible_card_combos(self, holecards: str, community_cards: str, game_type: str) -> list:
        """
        Since two cards must be used in PLO games, we need to set constraints for it

        Returns a list of possible combinations of 5 card sets that can be made from the holecards and community cards
        """
        if game_type == 'nlh':
            return ["".join(i) for i in combinations(holecards + community_cards, 5)]
        possible_cards = []
        if isinstance(holecards, str):
            holecards = [holecards[i: i + 2]
                         for i in range(0, len(holecards), 2)]
        for hc in combinations(holecards, 2):
            for cc in combinations(community_cards, 3):
                possible_cards.append(hc + cc)
        return ["".join(i) for i in possible_cards]

    def strength_evaluation(self, holecards: list, community_cards: list, game_type='plo4') -> tuple:
        """
        Perform a pairwise comparison of cards
        """
        if isinstance(holecards, str):
            holecards = [holecards[i:i + 2]
                         for i in range(0, len(holecards), 2)]
        if isinstance(community_cards, str):
            community_cards = [community_cards[i:i + 2]
                               for i in range(0, len(community_cards), 2)]
        all_cards = self.get_possible_card_combos(
            holecards, community_cards, game_type)
        combos = {i: self.card_strength_evaluator(i) for i in all_cards}
        values = sorted(combos.items(), key=lambda x: (
            x[1][1], x[1][2]), reverse=True)[0]
        return values[0], values[1][0], values[1][1], values[1][2], values[1][3]

    def get_playerwise_evaluation(self, holecards: str, community_cards: str, game_type: str) -> list:
        """
        Get playerwise card evaluations
        Acts as a wrapper for strength_evaluation

        Returns a list containing following items
            1. Rank of the combination (1 - 10)
            2. Name of the winning combination
            3. Rank of the winning combination
            4. Name of the highest card in the winning combination
            5. Rank of the highest card in the winning combination
        """
        winning_combo, winning_combo_name, winning_combo_rank, high_card_rank, high_card_name = self.strength_evaluation(
            holecards, community_cards, game_type)
        return [winning_combo, winning_combo_name, winning_combo_rank, high_card_name, high_card_rank]

    def find_intersection(self, cards1, cards2) -> str:
        """Find intersection between two sets of cards"""
        if isinstance(cards1, str):
            cards1 = [cards1[i: i+2] for i in range(0, len(cards1), 2)]

        if isinstance(cards2, str):
            cards2 = [cards2[i: i+2] for i in range(0, len(cards2), 2)]

        set1 = set(cards1)
        set2 = set(cards2)
        return "".join(set1.intersection(set2))

    def declare_winner(self, player_cards: dict, community_cards: str, game_type: str, return_type: str = 'list') -> list:
        """
        Given a set of cards, determine the winner

        Inputs:
            player_cards: Dictionary of player cards with player names (p1, p2... pn) as keys and card combinations as values
            community_cards: String of community cards
            game_type: Type of game

        Returns a list of dictionaries with following keys
            'best_combo': Best combination of cards
            'best_combo_name': Name of the best combination
            'best_combo_rank': Rank of the best combination
            'community_cards': Community cards
            'community_cards_used': Community cards used in making the best combination
            'high_rank': Highest rank of the best combination
            'high_rank_card': Name of the card with the highest rank
            'holecards': Hole cards
            'holecards_used': Hole cards used in making the best combination
            'player': Player number (p1 - p9)
            'winner': Boolean value indicating whether the player is the winner
        """
        strengths = dict()
        for k, holecard in player_cards.items():
            strengths[k] = self.get_playerwise_evaluation(
                holecard, community_cards=community_cards, game_type=game_type)
            holecards_used = self.find_intersection(holecard, strengths[k][0])
            community_cards_used = self.find_intersection(
                community_cards, strengths[k][0])
            strengths[k].append(holecard)
            strengths[k].append(holecards_used)
            strengths[k].append(community_cards_used)
        return_dict = dict()

        highest_combo = -1
        highest_rank = -1
        for k in strengths:
            return_dict[k] = {
                'best_combo': strengths[k][0],
                'best_combo_rank': strengths[k][2],
                'best_combo_name': strengths[k][1],
                'holecards': strengths[k][5],
                'community_cards': community_cards,
                'holecards_used': strengths[k][6],
                'community_cards_used': strengths[k][7],
                'high_rank': strengths[k][4],
                'high_rank_card': strengths[k][3]
            }
            highest_combo = max(highest_combo, strengths[k][2])
            highest_rank = max(highest_rank, strengths[k][4])

        for k, v in return_dict.items():
            if v["best_combo_rank"] == highest_combo and v["high_rank"] == highest_rank:
                v.update(
                    {
                        "player": k,
                        "winner": True
                    }
                )
            else:
                v.update({
                    "player": k,
                    "winner": False
                })
        if return_type == 'list':
            return [v for v in return_dict.values()]
        elif return_type == 'dict':
            return return_dict


if __name__ == '__main__':
    ev = Evaluator()
    one_pair = "AsAh8cTh9s"
    two_pair = "AsAhTcTh7c"
    three_of_a_kind = "AsAhAcTh4d"
    full_house = "AsAhAcThTc"
    four_of_a_kind = "AsAhAcAhTc"
    straight1 = "As2h3c4d5s"
    straight2 = "ThJcQdKdAh"
    flush = "Ah2h3h4h7h"
    straight_flush = "Ah2h3h4h5h"
    royal_flush = "AhKhQhJhTh"
    print(ev._is_one_pair(one_pair))
    print(ev._is_two_pair(two_pair))
    print(ev._is_three_of_a_kind(three_of_a_kind))
    print(ev._is_full_house(full_house))
    print(ev._is_four_of_a_kind(four_of_a_kind))
    print(ev._is_straight(straight1))
    print(ev._is_straight(straight2))
    print(ev._is_flush(flush))
    print(ev._is_straight_flush(straight_flush))
    print(ev._is_royal_flush(royal_flush))
    print(ev.card_strength_evaluator(one_pair))
    print(ev.card_strength_evaluator(two_pair))
    print(ev.card_strength_evaluator(three_of_a_kind))
    print(ev.card_strength_evaluator(full_house))
    print(ev.card_strength_evaluator(four_of_a_kind))
    print(ev.card_strength_evaluator(straight1))
    print(ev.card_strength_evaluator(straight2))
    print(ev.card_strength_evaluator(flush))
    print(ev.card_strength_evaluator(straight_flush))
    print(ev.card_strength_evaluator(royal_flush))
