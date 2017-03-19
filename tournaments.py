from match import Seed, Loser

def singleElimination(teams, matchFormat, numTeams = None):
    if numTeams == None:
        numTeams = len(teams)
    if numTeams == 1:
        return Seed(teams)
    return matchFormat(
            singleElimination(teams, matchFormat, numTeams // 2),
            singleElimination(teams, matchFormat, numTeams // 2)
            )

def doubleElimination(upperTeams, lowerTeams, matchFormat, numTeams = None):
    if numTeams == 2:
        return singleElimination(upperTeams + lowerTeams, matchFormat)
    else:
        return doubleElimination
    upperBracketFinal = matchFormat(Seed(upperTeams), Seed(upperTeams))
    lowerBracketFinal = matchFormat(
            matchFormat(Seed(lowerTeams), Seed(lowerTeams)),
            FromUpperBracket(upperBracketFinal)
            )
    grandFinal = matchFormat(upperBracketFinal, lowerBracketFinal)
    return grandFinal

def doubleElimination(upperTeams, lowerTeams, matchFormat, numTeams = None):
    if numTeams == None:
        numTeams = len(upperTeams)
        upperTeams = [Seed(upperTeams) for t in upperTeams]
        lowerTeams = [Seed(lowerTeams) for t in lowerTeams]
    if len(upperTeams) == 1:
        return matchFormat(upperTeams[0], lowerTeams[0])
    firstHalfUpper, secondHalfUpper = splitInHalves(upperTeams)
    firstHalfLower, secondHalfLower = splitInHalves(lowerTeams)
    upperMatches = [matchFormat(t1, t2) for (t1, t2) in zip(firstHalfUpper, secondHalfUpper)]
    upperLosers = [Loser(match) for match in upperMatches]
    lowerSurvivors = [matchFormat(t1, t2) for (t1, t2) in zip(firstHalfLower, secondHalfLower)]
    lowerWinners = [matchFormat(t1, t2) for (t1, t2) in zip(upperLosers, lowerSurvivors)]
    return doubleElimination(upperMatches, lowerWinners, matchFormat, numTeams // 2)

def splitInHalves(array):
    return array[:len(array)//2], array[len(array)//2:]
