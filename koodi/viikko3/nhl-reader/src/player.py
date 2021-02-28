class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = int(goals)
        self.assists = int(assists)
        self.nationality = nationality
        self.total = self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.total:2}"
