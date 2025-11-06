from collections import deque

class PokerException(Exception):
    def __init__(self,message, error_code):
        super().__init__(self.message)
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

class Player:
    def __init__(self, position, name):
        self._positions = [i for i in range(1,8)]
        self._position = position

    @property
    def position(self):
        return self._position
        
    @position.setter
    def position(self, value):
        if value not in self._positions:
            raise PokerException("Player position {value} falls outside game" \
            "limits\n Player position limits: {self._positions}", 300)
    
    def __str__(self):
        return f"Player {self.position}: {self.name}\n"


class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self._suits = ["Hearts", "Spades", "Diamonds", "Clubs", "Joker"]
        self._ranks = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Ace", "Joker"]

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if value not in self.suits:
            raise PokerException("Incorrect card suit: {value}\nSuit should be"\
            "one of the following: {self.suits}\n", 100)
        else:
            self._suit = value

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, value):
        if value not in self.ranks:
            raise PokerException("Incorrect card rank: {value}\nRank should be" \
            "one of the following: {self.ranks}\n", 200)
        else:
            self._rank = value
    
    def __str__(self):
        return f"Card: {self._suit} {self._rank}\n"
    
    def is_joker(self):
        return self._rank == "Joker"


class Deck:
    def __init__(self, include_joker=True, num_jokers=2):
        self._suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self._ranks = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Ace"]

        # Build the deck
        self.deck = deque([Card(s, r) for s in self._suits for r in self._ranks])

        # Include joker
        if include_joker:
            self.deck.extend([Card("Joker", "Joker") for _ in range(num_jokers)])
    
    def __len__(self):
        return len(self.deck)
    
    def __str__(self):
        return f"Current Deck: {self.deck}\n"
    
    def shuffle_deck(self):
        pass


class Game:
    def __init__(self, num_players, include_joker, num_jokers):
        # Stacks with moves that have been played
        self._card_stack = deque([])
        self._current_move = deque([])

        # Player variables
        self._players = [Player(i) for i in range(1,num_players + 1)]
        self._num_players = num_players

        # Deck variables
        self._deck = Deck(include_joker, num_jokers)
        self._deck.shuffle_deck()

        # Round and turn variables
        self._turn = 1
        self._round = 1

    def is_legal(self):
        pass

    def update_turn(self, skips):
        # Have a way to update turns even when its roundtable
        pass

    def kick_back(self):
        pass

    def draw_cards(self, num_draws):
        pass

    def move(self):
        pass

    def is_winner(self):
        pass

    def end_game(self):
        pass


