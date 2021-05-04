from Pack import Pack
from Player import Player
from Pile import Pile 

class GM:
    def __init__(self, names):
        self.pack = Pack()
        self.nbPlayers = len(names)
        self.players = []
        for i in range(self.nbPlayers):
            self.players.append(Player(names[i]))
        toDistribute = self.pack.distribute(self.nbPlayers)
        for i in range(len(toDistribute)):
            for j in toDistribute[i]:
                self.players[i].recieve(j)
        self.pile = Pile(self.pack.pick())
        self.turn = 0
        self.clockwise = True

    def addPlayer(self, name):
        newPlayer = Player(name)
        self.nbPlayers += 1
        for i in self.pack.distribute(1)[0]:
            newPlayer.recieve(i)
        self.players.append(newPlayer)

    def showHands(self):
        for i in self.players:
            print(i.showHand())
    
    def showGame(self):
        print(self.pack.showPack())
        self.showHands()

    def playTurn(self):
        p = self.players[self.turn]
        print("It is " + p.name + "'s turn to play")
        print("your hand:", p.showHand())
        print('pile:', self.pile.showTop())
        print("what would you like to do ? (type your action, no additional instructions given)")
        action = input()
        if ("pick" in action):
            c = self.cards.pick()
            if (c == "no cards"):
                self.cards.add(self.pile.empty())
                c = self.cards.pick()
            p.recieve(c)
            print(p.name+" has recieved:", c)
        elif ("place" in action or "put" in action):
            pass

def main():
    gm = GM(["paul", "dom", "nico"])
    # gm.showGame()
    gm.playTurn()

if __name__ == "__main__":
    main()