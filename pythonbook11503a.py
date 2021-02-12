from random import shuffle

class Card : 
    suits = [ "Clubs" , "Diamonds" , "Hearts" , "Spades" , ]
    values = [ "None" , "None" , "2" , "3" , "4" , "5" , "6"  , 
               "7" , "8" , "9" , "10" , "Jack" , "Queen" , "King" , "Ace" ] 
    def __init__ ( self , v , s ) :
        """カードクラスではスート（マーク）も値も整数値です。"""
        self.value = v 
        self.suit = s 
    def __lt__ ( self , c2 ) :
        if self.value < c2.value :
            return True 
        if self.value == c2.value :
            return self.suit < c2.suit 
        return False        
    def __gt__ ( self , c2 ) :
        if self.value > c2.value :
            return True 
        if self.value == c2.value :
            return self.suit > c2.suit 
        return False
    def __repr__ (self) :
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self) :
        self.cards = [] 
        for i in range ( 2, 15 ) :
            for j in range ( 0 , 4 ) :
                self.cards.append(Card(i,j)) 
        shuffle( self.cards )
    def draw(self) :
        if len(self.cards) == 0 :
            return 
        return self.cards.pop()

class Player :
    def __init__( self , name ) :
        self.wins = 0 
        self.card = None 
        self.name = name 

class Game : 
    def __init__ ( self , name1 = "Meaningless1", name2 = "Meaningless2") :
        self.deck = Deck ()
        self.p1 = Player(name1) 
        self.p2 = Player(name2)
    def print_winner ( self , winner ) :
        print ( "このラウンドは{}が勝ちました。".format( winner ) ) 
    def print_draw( self , p1 , p2 ) :
        print ( "{}は{}を引きました。他方、{}は{}を引きました。".format( p1.name , p1.card , p2.name , p2.card ) )
    def play_game(self) :
        cards = self.deck.cards
        print ( "ゲームを開始します。")
        while len(cards) >= 2 :
            self.p1.card = self.deck.draw() 
            self.p2.card = self.deck.draw() 
            self.print_draw( self.p1 , self.p2 )
            if self.p1.card > self.p2.card :
                self.p1.wins += 1 
                self.print_winner(self.p1.name)
            else :
                self.p2.wins += 1 
                self.print_winner(self.p2.name)
        print ( self.winner( self.p1 , self.p2 ) )
    def winner( self , p1, p2 ) :
        if   p1.wins > p2.wins :
            return "ゲーム終了、{}の勝利です。".format(p1.name)
        elif p1.wins < p2.wins :
            return "ゲーム終了、{}の勝利です。".format(p2.name)
        return "引き分け！！ご苦労様でした。"