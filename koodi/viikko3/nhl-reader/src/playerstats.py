from playerreader import PlayerReader


class PlayerStats:

    def __init__(self, reader=PlayerReader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nation):
        players_new = []

        for player in self.players:
            if player.nationality == nation:
                players_new.append(player)

        players_new.sort(key=lambda x: x.total, reverse=True)

        return players_new
