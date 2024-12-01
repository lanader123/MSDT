

class TennisGameDefactored1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        result = ""
        tempScore=0
        if (self.p1points==self.p2points):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
                3 : "Forty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            if (minusResult==1):
                result ="Advantage " + self.player1Name
            elif (minusResult ==-1):
                result ="Advantage " + self.player2Name
            elif (minusResult>=2):
                result = "Win for " + self.player1Name
            else:
                result ="Win for " + self.player2Name
        else:
            for i in range(1,3):
                if (i==1):
                    tempScore = self.p1points
                else:
                    result+="-"
                    tempScore = self.p2points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        return result


class TennisGameDefactored2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
    
    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 4):
            if (self.p1points==0):
                result = "Love"
            if (self.p1points==1):
                result = "Fifteen"
            if (self.p1points==2):
                result = "Thirty"
            if (self.p1points==3):
                result = "Forty"
            result += "-All"
        if (self.p1points==self.p2points and self.p1points>3):
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = "Fifteen"
            if (self.p1points==2):
                P1res = "Thirty"
            if (self.p1points==3):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = "Fifteen"
            if (self.p2points==2):
                P2res = "Thirty"
            if (self.p2points==3):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res="Thirty"
            if (self.p1points==3):
                P1res="Forty"
            if (self.p2points==1):
                P2res="Fifteen"
            if (self.p2points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res="Thirty"
            if (self.p2points==3):
                P2res="Forty"
            if (self.p1points==1):
                P1res="Fifteen"
            if (self.p1points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.p1points +=1
    
    
    def P2Score(self):
        self.p2points +=1
        
class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0
        
    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1
    
    def score(self):
        if (self.p1 < 4 and self.p2 < 4):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s



        # test support code
        def params(funcarglist):
            def wrapper(function):
                function.funcarglist = funcarglist
                return function
            return wrapper

        def pytest_generate_tests(metafunc):
            for funcargs in getattr(metafunc.function, 'funcarglist', ()):
                if "p1Name" not in funcargs:
                    funcargs["p1Name"] = "player1"
                if "p2Name" not in funcargs:
                    funcargs["p2Name"] = "player2"
                metafunc.addcall(funcargs=funcargs)

        # actual test code
        class TestTennis:

            @params([dict(p1Points=0, p2Points=0, score="Love-All"),
                     dict(p1Points=1, p2Points=1, score="Fifteen-All"),
                     dict(p1Points=2, p2Points=2, score="Thirty-All"),
                     dict(p1Points=3, p2Points=3, score="Forty-All"),
                     dict(p1Points=4, p2Points=4, score="Deuce"),

                     dict(p1Points=1, p2Points=0, score="Fifteen-Love"),
                     dict(p1Points=0, p2Points=1, score="Love-Fifteen"),
                     dict(p1Points=2, p2Points=0, score="Thirty-Love"),
                     dict(p1Points=0, p2Points=2, score="Love-Thirty"),
                     dict(p1Points=3, p2Points=0, score="Forty-Love"),
                     dict(p1Points=0, p2Points=3, score="Love-Forty"),
                     dict(p1Points=4, p2Points=0, score="Win for player1"),
                     dict(p1Points=0, p2Points=4, score="Win for player2"),

                     dict(p1Points=2, p2Points=1, score="Thirty-Fifteen"),
                     dict(p1Points=1, p2Points=2, score="Fifteen-Thirty"),
                     dict(p1Points=3, p2Points=1, score="Forty-Fifteen"),
                     dict(p1Points=1, p2Points=3, score="Fifteen-Forty"),
                     dict(p1Points=4, p2Points=1, score="Win for player1"),
                     dict(p1Points=1, p2Points=4, score="Win for player2"),

                     dict(p1Points=3, p2Points=2, score="Forty-Thirty"),
                     dict(p1Points=2, p2Points=3, score="Thirty-Forty"),
                     dict(p1Points=4, p2Points=2, score="Win for player1"),
                     dict(p1Points=2, p2Points=4, score="Win for player2"),

                     dict(p1Points=4, p2Points=3, score="Advantage player1"),
                     dict(p1Points=3, p2Points=4, score="Advantage player2"),
                     dict(p1Points=5, p2Points=4, score="Advantage player1"),
                     dict(p1Points=4, p2Points=5, score="Advantage player2"),
                     dict(p1Points=15, p2Points=14, score="Advantage player1"),
                     dict(p1Points=14, p2Points=15, score="Advantage player2"),

                     dict(p1Points=6, p2Points=4, score="Win for player1"),
                     dict(p1Points=4, p2Points=6, score="Win for player2"),
                     dict(p1Points=16, p2Points=14, score="Win for player1"),
                     dict(p1Points=14, p2Points=16, score="Win for player2"),

                     dict(p1Points=6, p2Points=4, score="Win for One", p1Name='One'),
                     dict(p1Points=4, p2Points=6, score="Win for Two", p2Name="Two"),
                     dict(p1Points=6, p2Points=5, score="Advantage One", p1Name='One'),
                     dict(p1Points=5, p2Points=6, score="Advantage Two", p2Name="Two"),
                     ])
            def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
                game = TennisGame(p1Name, p2Name)
                for i in range(p1Points):
                    game.won_point(p1Name)
                for i in range(p2Points):
                    game.won_point(p2Name)
                assert score == game.score()

