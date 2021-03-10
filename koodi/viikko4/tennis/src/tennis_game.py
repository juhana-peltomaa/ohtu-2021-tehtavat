SCORES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score_name(self, score):
        return SCORES[score]

    def get_player_score(self):
        player1_score_name = self.get_score_name(self.player1_score)
        player2_score_name = self.get_score_name(self.player2_score)
        return player1_score_name + "-" + player2_score_name

    def get_draw_score(self):
        if self.player1_score < 4:
            score = self.get_score_name(self.player1_score)
            print(score)
            return score + "-All"
        else:
            return "Deuce"

    def get_winning_score(self):
        minus_result = self.player1_score - self. player2_score

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_draw_score()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_winning_score()

        else:
            return self.get_player_score()
