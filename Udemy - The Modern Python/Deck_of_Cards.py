from random import choice, shuffle


class Card:

    values = ('A', 'Q', 'J', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    suits = ('Diamonds', 'Spades', 'Clubs', 'Hearts')

    def __init__(self):
        pass

    def __repr__(self):
        return f"{choice(Card.values)} of {choice(Card.suits)}"


class Deck:

    cards = []

    def __init__(self):
        for i in Card.values:
            for j in Card.suits:
                Deck.cards.append(f"{i} of {j}")

    def __repr__(self):
        return f"Deck of {self.count()} Cards"

    def count(self):
        return len(Deck.cards)

    def _deal(self, num):
        if self.count() != 0:

            if self.count() >= num:
                print([Deck.cards.pop() for i in range(1, num+1)])

            elif self.count() < num:
                print([Deck.cards.pop() for i in range(0, self.count())])

        else:
            raise ValueError('All cards have been dealt!')

    def shuffle(self):
        if len(Deck.cards) == 52:
            shuffle(Deck.cards)

        else:
            raise ValueError('Only full decks can be shuffled!')

    def deal_card(self):
        self._deal(1)

    def deal_hand(self, amount=1):
        if amount >= self.count():
            hands = []
            hands.append(self._deal(amount))
        else:
            raise IndexError("Cards amount out of range!")


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
my_deck.deal_card()
my_deck.deal_hand(60)
print(my_deck)
