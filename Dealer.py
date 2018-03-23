import numpy as np
class Cardgame(object):
    def __init__(self,deckqty):
        Deck = ["A-h","2-h","3-h","4-h","5-h","6-h","7-h","8-h","9-h","10-h","J-h","Q-h","K-h","A-s","2-s","3-s","4-s","5-s","6-s","7-s","8-s","9-s","10-s","J-s","Q-s","K-s","A-c","2-c","3-c","4-c","5-c","6-c","7-c","8-c","9-c","10-c","J-c","Q-c","K-c","A-d","2-d","3-d","4-d","5-d","6-d","7-d","8-d","9-d","10-d","J-d","Q-d","K-d"]
        self.DD = Deck
        n=1
        while(n<int(deckqty)):
            self.DD = np.append(self.DD,Deck)
            n=n+1
        np.random.shuffle(self.DD)
        self.CardsDrawn=0
        #print(self.DD)
    def SeeDeck(self):
        print(self.DD)
    def DealCards(self,n):
        Cards = []
        while(n>0):
            Cards = np.append(Cards,self.DD[self.CardsDrawn])
            self.CardsDrawn = self.CardsDrawn + 1
            n=n-1
        return(Cards)
            



