

class TennisGameDefactored1:


    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        
    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1
    
    def score(self):
        result = ""
        tempScore = 0
        if (self.player1_points == self.player2_points):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
                3 : "Forty-All",
            }.get(self.player1_points, "Deuce")
        elif (self.player1_points >= 4 or self.player2_points >= 4):
            minusResult = self.player1_points - self.player2_points
            if (minusResult == 1):
                result ="Advantage " + self.player1_name
            elif (minusResult == -1):
                result ="Advantage " + self.player2_name
            elif (minusResult >= 2):
                result = "Win for " + self.player1_name
            else:
                result ="Win for " + self.player2_name
        else:
            for i in range(1, 3):
                if (i == 1):
                    tempScore = self.player1_points
                else:
                    result += "-"
                    tempScore = self.player2_points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        return result


class TennisGameDefactored2:


    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0


    def won_point(self, playerName):
        if playerName == self.player1_name:
            self.player1_score()
        else:
            self.player2_score()


    def score(self):
        result = ""
        if (self.player1_points == self.player2_points and self.player1_points < 4):
            if (self.player1_points == 0):
                result = "Love"
            if (self.player1_points == 1):
                result = "Fifteen"
            if (self.player1_points == 2):
                result = "Thirty"
            if (self.player1_points == 3):
                result = "Forty"
            result += "-All"
        if (self.player1_points == self.player2_points and self.player1_points>3):
            result = "Deuce"
        
        player1_result = ""
        player2_result = ""
        if (self.player1_points > 0 and self.player2_points == 0):
            if (self.player1_points == 1):
                player1_result = "Fifteen"
            if (self.player1_points == 2):
                player1_result = "Thirty"
            if (self.player1_points == 3):
                player1_result = "Forty"
            player2_result = "Love"
            result = player1_result + "-" + player2_result
        if (self.player2_points > 0 and self.player1_points == 0):
            if (self.player2_points == 1):
                player2_result = "Fifteen"
            if (self.player2_points == 2):
                player2_result = "Thirty"
            if (self.player2_points == 3):
                player2_result = "Forty"
            
            player1_result = "Love"
            result = player1_result + "-" + player2_result
        
        
        if (self.player1_points > self.player2_points and self.player1_points < 4):
            if (self.player1_points == 2):
                player1_result="Thirty"
            if (self.player1_points == 3):
                player1_result="Forty"
            if (self.player2_points == 1):
                player2_result="Fifteen"
            if (self.player2_points == 2):
                player2_result="Thirty"
            result = player1_result + "-" + player2_result
        if (self.player2_points > self.player1_points and self.player2_points < 4):
            if (self.player2_points == 2):
                player2_result="Thirty"
            if (self.player2_points == 3):
                player2_result="Forty"
            if (self.player1_points == 1):
                player1_result="Fifteen"
            if (self.player1_points == 2):
                player1_result="Thirty"
            result = player1_result + "-" + player2_result
        
        if (self.player1_points > self.player2_points and self.player2_points >= 3):
            result = "Advantage " + self.player1_name
        
        if (self.player2_points > self.player1_points and self.player1_points >= 3):
            result = "Advantage " + self.player2_name
        
        if (self.player1_points >= 4 and self.player2_points >= 0 and
                (self.player1_points - self.player2_points) >= 2):
            result = "Win for " + self.player1_name
        if (self.player2_points >= 4 and self.player1_points >= 0 and
                (self.player2_points - self.player1_points) >= 2):
            result = "Win for " + self.player2_name
        return result


    def SetPlayer1Score(self, number):
        for i in range(number):
            self.player1_score()


    def SetPlayer2Score(self, number):
        for i in range(number):
            self.player2_score()


    def player1_score(self):
        self.player1_points += 1
    
    
    def player2_score(self):
        self.player2_points += 1


class TennisGameDefactored3:
    def __init__(self, player1_name, player2_name):
        self.p1N = player1_name
        self.p2N = player2_name
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
            return s + "-All" if (self.p1 == self.p2) else s + \
                                                           "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2) *
                    (self.p1-self.p2) == 1) else "Win for " + s


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
                     dict(p1Points=15, p2Points=14,
                          score="Advantage player1"),
                     dict(p1Points=14, p2Points=15,
                          score="Advantage player2"),

                     dict(p1Points=6, p2Points=4, score="Win for player1"),
                     dict(p1Points=4, p2Points=6, score="Win for player2"),
                     dict(p1Points=16, p2Points=14, score="Win for player1"),
                     dict(p1Points=14, p2Points=16, score="Win for player2"),

                     dict(p1Points=6, p2Points=4,
                          score="Win for One", p1Name='One'),
                     dict(p1Points=4, p2Points=6,
                          score="Win for Two", p2Name="Two"),
                     dict(p1Points=6, p2Points=5,
                          score="Advantage One", p1Name='One'),
                     dict(p1Points=5, p2Points=6,
                          score="Advantage Two", p2Name="Two"),
                     ])
            def test_get_score(self, p1_points, p2_points,
                               score, p1_name, p2_name):
                game = TennisGame(p1_name, p2_name)
                for i in range(p1_points):
                    game.won_point(p1_name)
                for i in range(p2_points):
                    game.won_point(p2_name)
                assert score == game.score()

