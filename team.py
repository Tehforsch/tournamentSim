class Team:
    idCounter = 0
    def __init__(self, rating):
        self.rating = rating
        self._id = Team.idCounter
        Team.idCounter += 1

    def winrate(self, team2):
        return 1 / (1 + 10 ** ((team2.rating - self.rating) / 400.0))

    def __str__(self):
        return "{} ({})".format(self._id, self.rating)
