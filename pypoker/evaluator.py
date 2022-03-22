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

    def _is_royal_flush(self, cards: list) -> bool:
        """
        Check if the cards are a royal flush
        """
        if self._is_straight_flush(cards) and self._is_royal(cards):
            return True
        return False

    def _is_straight_flush(self, cards: list) -> bool:
        """
        Check if the cards are a straight flush
        """
        if self._is_flush(cards) and self._is_straight(cards):
            return True
        return False

    def _is_royal(self, cards: list) -> bool:
        """
        Check if the highest card is Ace
        """
        if cards[0][0] == 'A':
            return True
        return False

    def _is_flush(self, cards: list) -> bool:
        """
        Check if the cards are a flush
        """
        if len(set([card[1] for card in cards])) == 1:
            return True
        return False

    def _is_straight(self, cards: list) -> bool:
        """
        Check if the cards form a straight
        """
        start = cards[0][0]
        end = cards[-1][0]
        slice = self.ranks[self.ranks.index(start):self.ranks.index(end) + 1]
        if len(slice) == 5:
            return True
        return False

    def _is_four_of_a_kind(self, cards: list) -> bool:
        """
        Check if the cards are four of a kind
        """
        if len(set([card[0] for card in cards])) == 2:
            return True

    def _is_full_house(self, cards: list) -> bool:
        """
        Check if the cards are a full house
        """
        if len(set([card[0] for card in cards])) == 2:
            ranks = [card[0] for card in cards]
            if ranks.count(ranks[0]) == 2 and ranks.count(ranks[1]) == 3:
                return True
            elif ranks.count(ranks[0]) == 3 and ranks.count(ranks[1]) == 2:
                return True
        return False

    def _is_three_of_a_kind(self, cards: list) -> bool:
        """
        Check if the cards are three of a kind
        """
        if len(set([card[0] for card in cards])) == 3:
            ranks = [card[0] for card in cards]
            if ranks.count(ranks[0]) == 3 or ranks.count(ranks[1]) == 3 or ranks.count(ranks[2]) == 3:
                return True
        return False

    def _is_two_pair(self, cards: list) -> bool:
        """
        Check if the cards are two pair
        """
        if len(set([card[0] for card in cards])) == 3:
            ranks = [card[0] for card in cards]
            counter = 0
            for rank in ranks:
                if ranks.count(rank) == 2:
                    counter += 1
            if counter == 2:
                return True
        return False

    def _is_one_pair(self, cards: list) -> bool:
        """
        Check if the cards are one pair
        """
        if len(set([card[0] for card in cards])) == 4:
            ranks = [card[0] for card in cards]
            if ranks.count(ranks[0]) == 2 or ranks.count(ranks[1]) == 2 or ranks.count(ranks[2]) == 2 or ranks.count(ranks[3]) == 2:
                return True
        return False

    def card_strength_evaluator(self, cards: list) -> tuple:
        """
        Given a set of cards, evaluate their strength and return the relevant information about it.

        Returns a tuple with following items

            1. Name of the combination
            2. Rank of the combination (1 - 10)
        """
        if isinstance(cards, str):
            cards = [cards[i: i + 2] for i in range(0, len(cards), 2)]
        if len(cards) != 5:
            raise ValueError("You must provide 5 cards")
        cards = sorted(cards, key=lambda x: self.rank_and_suites.index(x))
        # Check for royal flush
        if self._is_royal_flush(cards):
            return self.card_strengths[1], 1
        # Check for straight flush
        elif self._is_straight_flush(cards):
            return self.card_strengths[2], 2
        # Check for four of a kind
        elif self._is_four_of_a_kind(cards):
            return self.card_strengths[3], 3
        # Check for full house
        elif self._is_full_house(cards):
            return self.card_strengths[4], 4
        # Check for flush
        elif self._is_flush(cards):
            return self.card_strengths[5], 5
        # Check for straight
        elif self._is_straight(cards):
            return self.card_strengths[6], 6
        # Check for three of a kind
        elif self._is_three_of_a_kind(cards):
            return self.card_strengths[7], 7
        # Check for two pair
        elif self._is_two_pair(cards):
            return self.card_strengths[8], 8
        # Check for one pair
        elif self._is_one_pair(cards):
            return self.card_strengths[9], 9
        # Check for high card
        else:
            return self.card_strengths[10], 10

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

    def _evaluate_best(self, card: str, current_best: str) -> str:
        """
        Evaluate cards of same level against higher ranks
        """
        sum_ranks_cards = sum([self.ranks.index(card[i])
                              for i in range(0, len(card), 2)])
        sum_ranks_current_best_cards = sum(
            [self.ranks.index(current_best[i]) for i in range(0, len(current_best), 2)])
        if sum_ranks_cards > sum_ranks_current_best_cards:
            return card
        elif sum_ranks_cards == sum_ranks_current_best_cards:
            sum_suites_cards = sum([self.suites.index(card[i])
                                   for i in range(1, len(card), 2)])
            sum_suites_current_best_cards = sum(
                [self.suites.index(current_best[i]) for i in range(1, len(current_best), 2)])
            if sum_suites_cards > sum_suites_current_best_cards:
                return card
            elif sum_suites_cards == sum_suites_current_best_cards:
                return card
            else:
                return current_best
        return current_best

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
        rank = 10
        combos = dict()
        all_cards = self.get_possible_card_combos(
            holecards, community_cards, game_type)
        current_best = all_cards[0]
        for card in all_cards:
            _, current_rank = self.card_strength_evaluator(card)
            if current_rank < rank:
                rank = current_rank
                current_best = card
            elif current_rank == rank:
                current_best = self._evaluate_best(card, current_best)
            combos[current_rank] = current_best
        return [combos[rank], rank, self.card_strengths[rank], self.get_high_rank(combos[rank])]

    def get_playerwise_evaluation(self, holecards: str, community_cards: str, game_type: str) -> list:
        """
        Get playerwise card evaluations
        Acts as a wrapper for strength_evaluation

        Returns a list containing following items
            1. Rank of the combination (1 - 10)
            2. Card combination
            3. Name of the combination
            4. Highest rank of the combination
        """
        rank, card, strength, high_rank = self.strength_evaluation(
            holecards, community_cards, game_type)
        return [rank, card, strength, high_rank]

    def get_high_rank(self, card: str) -> int:
        """
        Get rank of the highest card in combo
        """
        card = sorted(card[::2], key=lambda x: self.ranks.index(x))
        return self.ranks.index(card[-1][0])

    def declare_winner(self, player_cards: dict, community_cards: str, game_type: str) -> list:
        """
        Given a set of cards, determine the winner

        Inputs:
            player_cards: Dictionary of player cards with player names (p1, p2... pn) as keys and card combinations as values
            community_cards: String of community cards
            game_type: Type of game

        Returns a list of dictionaries with following keys
            'best_combo': Best combination of cards
            'best_combo_rank': Rank of the best combination
            'best_combo_name': Name of the best combination
            'holecards': Hole cards
            'community_cards': Community cards
            'holecards_used': Hole cards used in making the best combination
            'community_cards_used': Community cards used in making the best combination
            'high_rank': Highest rank of the best combination
            'player_number': Player number (1 - 9)
            'winner': Boolean value indicating whether the player is the winner
        """
        strengths = dict()
        for k, holecard in player_cards.items():
            strengths[k] = self.get_playerwise_evaluation(
                holecard, community_cards=community_cards, game_type=game_type)
        for k in player_cards:
            strengths[k].append(player_cards[k])
        return_dict = dict()

        for k in player_cards:
            holecards_list = set([strengths[k][4][i:i + 2]
                                 for k in strengths for i in range(0, len(strengths[k][4]), 2)])
            community_cards_list = set(
                [community_cards[i:i + 2] for i in range(0, len(community_cards), 2)])
            winning_combo_list = set([strengths[k][0][i:i+2]
                                     for i in range(0, len(strengths[k][0]), 2)])

            holecards_used = "".join(
                holecards_list.intersection(winning_combo_list))
            community_cards_used = "".join(community_cards_list.intersection(
                winning_combo_list))

            return_dict[k] = {
                'best_combo': strengths[k][0],
                'best_combo_rank': strengths[k][1],
                'best_combo_name': strengths[k][2],
                'holecards': strengths[k][4],
                'community_cards': community_cards,
                'holecards_used': holecards_used,
                'community_cards_used': community_cards_used,
                'high_rank': strengths[k][3],
                'winner': False
            }
        del strengths
        ranks = [return_dict[k]['best_combo_rank'] for k in player_cards]
        lowest_rank = min(ranks)
        if ranks.count(lowest_rank) == 1:
            for k, v in return_dict.items():
                if v['best_combo_rank'] == lowest_rank:
                    v['winner'] = True
        else:
            winners = {k: v for k, v in return_dict.items(
            ) if v['best_combo_rank'] == lowest_rank}
            higher_rank = max([winners[k]['high_rank'] for k in winners])
            for k, v in winners.items():
                if v['high_rank'] == higher_rank:
                    v['winner'] = True
                else:
                    v['winner'] = False
        for k, v in return_dict.items():
            v['player_number'] = int(k[-1])

        return [v for v in return_dict.values()]


if __name__ == '__main__':
    pass
