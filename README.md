# PyPoker

## What is it?
This is a simple python library for poker things. It's supposed to be a fully fledged poker engine, but that's in the to-do list. As of now, this library has three classes - Deck, Evalutator and Poker. As of now, it supports Texas Hold'em, Pot Limit Omaha 4 card, Pot Limit Omaha 5 card and Pot Limit Omaha 6 card.

## What is Deck?
Deck is a class that represents a deck of cards. It relies on ```random``` library for random sampling - which is not very secure way of doing things. However, it works as of now. The deck supports having multiple decks of cards - which was designed to be extensible to other card games such as Rummy.

The main method of Deck class is ```deal_poker_hands```. Its description is as below

```
Return a dictionary of poker hands based on game type

Dictionary contains the following key-value pairs:
    'community_cards': list of community cards
    'player_cards': dictionary of player cards
    'variant': game variant
    'flop': string of flop cards
    'turn': string of turn card
    'river': string of river card

Players are referred by the literals p1, p2... pn
```
## What is Evaluator?
Evaluator is a class that is used to evaluate poker combinations and return the winning combination. It's fairly simple and uses the simplest algorithm to evaluate the poker hands. It's certainly not the fastest way out there, nor is it free of bugs, but it works as of now. The benchmark I could get for the current features on my underpowered PC is: ```Total time taken for 1000 iterations: 11.37 s``` Future versions would be made to improve the performance and add more features and remove the bugs.

The main method of Evaluator class is ```declare_winner```, the description of which is given below
```
Given a set of cards, determine the winner
Inputs:
    player_cards: Dictionary of player cards with p1, p2... pn as keys and holecards as values
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
    'winner': Boolean value indicating if the player is the winner

```

## What is Poker?
Poker essentially acts as a wrapper for these two classes (as of now). In future updates, it would support actually playing the game (through CLI, or a GUI if I can find a decent enthusiastic friend to help me out with it). The two methods of Poker class are ```deal()``` and ```declare_winner()```, which are essentially an abstraction of the methods of the classes above.

## What are the plans for future?
In future, I'd like to add the functionality of running Monte Carlo simulations on playing cards, determining the probability, as well as parsing hand history files and statistically determining preflop losses. I'd also like to add the full fledged gaming capabilities to this library.

---


### Side note
As you may have guessed, I suck at writing documentation. So, if you have any doubts or suggestions, drop me a mail at [animesh-srivastava](mailto:animesh.srivastava.1999@gmail.com).



