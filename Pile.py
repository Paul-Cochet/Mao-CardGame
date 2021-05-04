class Pile:
    def __init__(self, card):
        self.cards=[card]
    
    def showPile(self):
        return self.cards
    
    def showTop(self):
        return self.cards[-2:]

    def place(self, card):
        self.cards.append(card)

    def cancelPlay(self):
        c = self.cards[-1]
        del self.cards[-1]
        return c

    def empty(self):
        c = self.cards[:-2]
        self.cards = self.cards[-2:]
        return c