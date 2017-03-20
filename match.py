import random

class Match:
    idCounter = 0
    def __init__(self, matches):
        self.matches = matches
        self._winner = None
        self._id = Match.idCounter
        Match.idCounter += 1

    @property
    def winner(self):
        self.teams = [match.winner for match in self.matches]
        if self._winner == None:
            self._winner = self.determineWinner()
        return self._winner

    @property
    def numGames(self):
        return self._numGames + sum(match.numGames for match in self.matches)

    def reset(self):
        self._winner = None
        for match in self.matches:
            match.reset()

class BestOf(Match):
    def __init__(self, maxGames, team1, team2):
        self.maxGames = maxGames
        assert self.maxGames % 2 == 1, "Even number in Best-Of match"
        self.numGamesToWin = (self.maxGames + 1) // 2
        super().__init__([team1, team2])

    def determineWinner(self):
        assert len(self.teams) == 2
        numWins1 = 0
        winrateTeam1 = self.teams[0].winrate(self.teams[1])
        numWins1 = 0
        for numGames in range(1, self.maxGames+1):
            team1Wins = random.random() < winrateTeam1
            if team1Wins:
                numWins1 += 1
            if numWins1 >= self.numGamesToWin:
                winner = self.teams[0]
                break
            if numGames - numWins1 >= self.numGamesToWin:
                winner = self.teams[1]
                break
        self._numGames = numGames
        return winner

    def __repr__(self):
        return "Bo{} {}".format(self.maxGames, self._id)

class Bo1(BestOf):
    def __init__(self, team1, team2):
        super().__init__(1, team1, team2)

class Bo3(BestOf):
    def __init__(self, team1, team2):
        super().__init__(3, team1, team2)

class Loser(Match):
    def __init__(self, match):
        self.match = match
        self.matches = match.matches
        assert isinstance(match, BestOf)

    @property
    def winner(self):
        if self.match.winner == self.match.teams[0]:
            return self.match.teams[1]
        else:
            return self.match.teams[0]

    def __repr__(self):
        return "Loser of {}".format(self.match)

    @property
    def numGames(self):
        return self.match.numGames

class Seed:
    def __init__(self, teams):
        self.teams = teams
        self.reset()
    
    @property
    def winner(self):
        chosenTeam = random.choice(self.toSeedFrom)
        self.toSeedFrom.remove(chosenTeam)
        return chosenTeam

    def reset(self):
        self.toSeedFrom = self.teams[:]

    def __repr__(self):
        return "Seed ({})".format(len(self.teams))

    @property
    def numGames(self):
        return 0
