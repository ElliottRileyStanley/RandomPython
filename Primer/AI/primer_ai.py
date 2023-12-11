import random
import shutil

strat = []
percent_changed = 0.1

def choice(heads, tails, flips, strat):
    if heads + tails > 20:
        return (random.randrange(1,2))
    else:
        return strat[int(((21*22/2)+1)*min(flips, 20)+((heads+tails)*(heads+tails+1)/2)+tails)]
    
def fitness(strat_file, iterations):
    global generations
    global percent_changed
    global heads
    global tails
    global record
    global flips
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
        cheater = bool(random.randrange(0,2))
        while flips >= 0 and points < 4000:
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
                cheater = bool(random.randrange(0,2))
            elif int(choice(heads, tails, flips, strat)) == 2:
                if cheater == False:
                    flips -= 30
                else:
                    flips += 15
                    points += 1
                heads = 0
                tails = 0
                cheater = bool(random.randrange(0,2))
        record.append(points)
    if strat_file == 1:
        percent_changed = max(1-sum(record)/iterations/2000, 0.0001)
    return int(sum(record)/iterations)

generations = int(input("How many generations? - "))
iterations = int(input("How many iterations per generation? - "))

for i in range(1, generations+1):
    strat = open(r'Primer\prevstrat.text').readlines()
    open(r'Primer\newstrat.text', 'w').write("")

    for x in range(0, len(strat)):
        if random.random() < percent_changed:
            strat[x] = str(random.randrange(0, 3)) + "\n"

    for item in strat:
        open(r'Primer\newstrat.text', 'a').write(str(item))

    if fitness(1, int(iterations*5-(percent_changed*5))) < fitness(2, int(iterations*5-(percent_changed*5))):
        shutil.copyfile(r'Primer\newstrat.text', r'Primer\prevstrat.text')
        print("Strat changed")
    else:
        print("Strat didn't change")
    print(str(i/generations))
    print(percent_changed)
    print("")