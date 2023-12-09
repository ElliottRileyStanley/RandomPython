import random
from pathlib import Path
strat = []

def choice(heads, tails, flips, strat):
    if heads + tails > 20:
        return (random.randrange(1,2))
    else:
        return strat[int(((21*22/2)+1)*min(flips, 20)+((heads+tails)*(heads+tails+1)/2)+tails)]
    
def fitness(strat_file, iterations):
    if strat_file == 1:
        strat = open(r'Primer\prevstrat.text').readlines()
    else:
        strat = open(r'Primer\newstrat.text').readlines()
    for x in range(0,len(strat)):
        strat[x] = strat[x][0]
    record = []
    flips = 100
    for x in range(0, iterations):
        flips = 100
        heads = 0
        tails = 0
        points = 0
        cheater = bool(random.randrange(0,1))
        while flips >= 0:
            if int(choice(heads, tails, flips, strat)) == 0:
                flips -= 1
                coin = random.randrange(1, 4)
                if cheater == True and coin > 1:
                    heads += 1
                elif cheater == True and coin == 1:
                    tails += 1
                elif cheater == False and coin >= 3:
                    heads += 1
                elif cheater == False and coin <= 2:
                    tails += 1
            elif int(choice(heads, tails, flips, strat)) == 1:
                if cheater == True:
                    flips -= 30
                else:
                    flips += 15
                    points += 1
                heads = 0
                tails = 0
                cheater = bool(random.randrange(0,1))
            elif int(choice(heads, tails, flips, strat)) == 2:
                if cheater == False:
                    flips -= 30
                else:
                    flips += 15
                    points += 1
                heads = 0
                tails = 0
                cheater = bool(random.randrange(0,1))
        record.append(points)
    return int(sum(record)/iterations)

print("Average points - " + str(fitness(1, 1000)))