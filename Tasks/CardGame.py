import random

class Cards:

    def koloda(self):
        self.kolod = []

        for i in range(1,37):
            self.kolod.append(i)
        return self.kolod

    def player1(self):
        for i in range(0,10):

            self.cards_of_player1=random.randint(0,36)
            print(self.cards_of_player1)
            return self.cards_of_player1

    def player2(self):
        for i in range(0, 10):
            self.cards_of_player2 = random.randint(0, 36)
            print(self.cards_of_player2)
            return self.cards_of_player2

    def competition(self):

        i=0
        while i<10:
            self.first_player = self.player1(Cards)
            self.second_player = self.player2(Cards)
            if self.first_player.__gt__(self.second_player):
                print ("success!")
                i = i+1
                continue
            elif self.first_player.__lt__(self.second_player):
                print(("looose"))
                break
            elif self.first_player.__eq__(self.second_player):
                print(("next try"))
                continue


Cards.competition(Cards)