import random
import constants
import tournaments
import match
from team import Team
from match import Seed
import visualization
import numpy as np

class TournamentRun:
    def __init__(self, title, tournament):
        self.tournament = tournament
        self.title = title

    def getWinProbabilities(self, teams):
        tournament = self.tournament(teams)
        winCount = [0 for t in teams]
        numGames = 0
        for n in range(constants.NUM_ITERATIONS):
            tournament.reset()
            winner = tournament.winner
            winCount[teams.index(winner)] += 1
            numGames += tournament.numGames
        self.numGames = numGames / constants.NUM_ITERATIONS
        self.probabilities = [wins / constants.NUM_ITERATIONS for wins in winCount]

def getTournamentData(tournament):
    data = []
    for elo in range(0, 400, 20):
        teams = [Team(elo)] + [Team(0) for i in range(7)]
        # printTree(t)
        tournament.getWinProbabilities(teams)
        data.append([teams[0].winrate(teams[1]), tournament.probabilities[0] / tournament.numGames])
    return np.array(data)

def printTree(node, depth = 0):
    print("-"*depth, node)
    if isinstance(node, Seed):
        return
    for match in node.matches:
        printTree(match, depth+1)

def plot(ts):
    data = []
    for t in ts:
        data.append((t.title, getTournamentData(t)))
    visualization.show(data, "winratePerGame.png")

ts = []
ts.append(TournamentRun("Double Elim Bo1", lambda teams: tournaments.doubleElimination(teams[:4], teams[4:], match.Bo1)))
ts.append(TournamentRun("Single Elim Bo1", lambda teams: tournaments.singleElimination(teams[:8], match.Bo1)))
ts.append(TournamentRun("Double Elim Bo3", lambda teams: tournaments.doubleElimination(teams[:4], teams[4:], match.Bo3)))
ts.append(TournamentRun("Single Elim Bo3", lambda teams: tournaments.singleElimination(teams[:8], match.Bo3)))
plot(ts)
