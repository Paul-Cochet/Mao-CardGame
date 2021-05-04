class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def recieve(self, card):
        self.hand.append(card)

    def showHand(self):
        return self.hand

    def playCard(self, card):
        if (card not in self.hand):
            return "impossible play"
        self.hand = list(filter(lambda x: x != card, self.hand))
        return card
