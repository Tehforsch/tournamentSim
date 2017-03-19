import random
import constants
import tournaments
import match
from team import Team
from match import Seed

def getWinProbabilities(tournament, teams):
    winCount = [0 for t in teams]
    for n in range(constants.NUM_ITERATIONS):
        tournament.reset()
        winner = tournament.winner
        winCount[teams.index(winner)] += 1
    return [wins / constants.NUM_ITERATIONS for wins in winCount]

def printTree(node, depth = 0):
    print("-"*depth, node)
    if isinstance(node, Seed):
        return
    for match in node.matches:
        printTree(match, depth+1)

teams = [Team(0) for i in range(8)]
t = tournaments.doubleElimination(teams[:4], teams[4:], match.Bo1)
# t = tournaments.singleElimination(teams[:4], match.Bo1)
printTree(t)
print(getWinProbabilities(t, teams))
