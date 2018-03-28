import Dealer as D
import numpy as np

class blackjack(object):
    def __init__(self,playernum,myposition=1,deckqty=1):
        self.dealer = D.Shuffle(deckqty)
        self.myposition = myposition
        stop=playernum+1
        self.visiblecards = []
        r = np.arange(1,stop)
        self.players = [["dealer",[]]]
        for x in r:
            addp=("player%s"%(x))
            self.players.append([str(addp),[]])
        for p,hand in self.players:
            carddealt=self.dealer.DealCards(1)
            hand.append(carddealt)
            self.visiblecards.append(carddealt)
            #draw1
        myhand = self.players[self.myposition][1]
        #print(myhand)
        #print(self.visiblecards)
        return(None)
    def CheckHand(self):
        myhand = self.players[self.myposition][1]
        return(myhand)

    def hit(self):
        return(card)

if __name__ == '__main__':
    deckqty='5'
    dealer = D.Shuffle(deckqty)

    #for h in hand:
    #    num,lost = h.split('-')
    #    number = np.append(number,num)