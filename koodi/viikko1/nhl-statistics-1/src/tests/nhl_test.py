import unittest
from statistics import Statistics
from player import Player

players = [
    Player("Semenko", "EDM", 4, 12),
    Player("Lemieux", "PIT", 45, 54),
    Player("Kurri",   "EDM", 37, 53),
    Player("Yzerman", "DET", 42, 56),
    Player("Gretzky", "EDM", 35, 89)
]


class PlayerReaderStub:
    def get_players(self):
        return players


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_haku(self):
        player = self.statistics.search("Gretzky")
        self.assertEqual(player, players[-1])

    def test_haku_vaara_nimi(self):
        player = self.statistics.search("Gretzky2")
        self.assertEqual(player, None)

    def test_points(self):
        from statistics import sort_by_points

        points = sort_by_points(players[-1])
        self.assertEqual(points, 124)

    def test_top_score(self):
        player = self.statistics.top_scorers(1)
        self.assertEqual(player[0], players[-1])

    def test_team(self):
        player = self.statistics.team("PIT")
        self.assertEqual(player[0], players[1])
