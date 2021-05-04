import random

class Pack:
    def __init__(self):
        self.cards = []
        self.fillSuit("spades")
        self.fillSuit("diamonds")
        self.fillSuit("hearts")
        self.fillSuit("clubs")
        self.shuffle()

    def add(self, cards):
        self.cards.append(cards)
        self.shuffle()

    def showPack(self):
        return self.cards

    def pick(self):
        if (len(self.cards) > 0):
            r = self.cards[0]
            del self.cards[0]
            return r
        else:
            return "no cards"

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, nbPlayers):
        self.shuffle()
        dis = [[] for i in range(nbPlayers)]
        for i in range(3):
            for p in dis:
                p.append(self.pick())
        return dis

    def fillSuit(self, sign):
        for i in range(1,10+1):
            self.cards.append(self.getSign(sign)+"%d" % i)
        self.cards.append(self.getSign(sign)+"J")
        self.cards.append(self.getSign(sign)+"Q")
        self.cards.append(self.getSign(sign)+"K")

    def getSign(self, sign):
        if (sign == "spades"):
            return "\u2660"
        if (sign == "diamonds"):
            return "\u2666"
        if (sign == "hearts"):
            return "\u2665"
        if (sign == "clubs"):
            return "\u2663"