import Dealer as D
import numpy as np
import math

def facecards(numlist):
    for n,val in enumerate(numlist):
            if(val == 'K') or (val == 'Q') or (val =='J'):
                numlist[n] = 10
            else:
                numlist[n] = numlist[n]
    return(numlist)

def aces(numlist):
    numlists = []
    if 'A' in numlist:
        aqty = numlist.count('A')
        filler = []
        finallen = 2**aqty
        an = 1
        while len(numlists) < finallen:
            numlists.append(filler)
        for val in numlist:
            if val is not 'A':
                n=0
                while(n+1<finallen):
                    numlists[n].append(val)
                    n=n+1
            else:
                q=0
                while(q<len(numlists)):
                    checker = math.ceil((q+1)/(2**(an-1)))
                    templist = []
                    templist = list(numlists[q])
                    #ODDEVEN IF ELIF ELSE ON CHECKER
                    if ((checker % 2) == 0):
                        aceval = 11
                        templist.append(aceval)
                        #Even
                    elif(((checker % 2) != 0)):
                        aceval = 1
                        templist.append(aceval)
                        #Odd
                    else:
                        print("dude I don't know")
                        pass
                    numlists[q] = list(templist)
                    q = q+1    
                an=an+1
        pass
    else:
        numlists = numlist
        #print("NO ACES")
        pass
    return(numlists)
    
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
            for val in carddealt:
                carddealt = val
            hand.append(carddealt)
            self.visiblecards.append(carddealt)
            #draw1
        for p,hand in self.players:
            carddealt=self.dealer.DealCards(1)
            for val in carddealt:
                carddealt = val
            hand.append(carddealt)
            if(p is self.players[self.myposition][0]):
                self.visiblecards.append(carddealt)
            else:
                pass
            #self.visiblecards.append(carddealt)    
        #myhand = self.players[self.myposition][1]
        #print(myhand)
        #print(self.visiblecards)
        return(None)

    def checkhand(self):
        myhand = self.players[self.myposition][1]
        return(myhand)

    def splitnums(self,playerpos):
        handnums = []
        for val in self.players[playerpos][1]:
            num,suit = val.split('-')
            handnums.append(num)
        return(handnums)

    def hit(self,playerpos):
        self.players[playerpos][1].append(self.dealer.DealCards(1))
        #return(card)
        #test2
        pass

if __name__ == '__main__':
    deckqty='5'
    dealer = D.Shuffle(deckqty)

    #for h in hand:
    #    num,lost = h.split('-')
    #    number = np.append(number,num)