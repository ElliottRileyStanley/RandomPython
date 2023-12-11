import random
import shutil

def fitness(strat):
    global possibilities
    possibilities = [{"heads":0, "tails":0, "flips":100, "cheater":True, "points":0, "chance":0.5},{"heads":0, "tails":0, "flips":100, "cheater":False, "points":0, "chance":0.5}]
    dead_possibilities = []
    while True:
        if possibilities[0]["heads"] + possibilities[0]["tails"] > 20:
            choice = (random.randrange(1,2))
        else:
            choice = strat[int(((21*22/2)+1)*min(possibilities[0]["flips"], 20)+((possibilities[0]["heads"]+possibilities[0]["tails"])*(possibilities[0]["heads"]+possibilities[0]["tails"]+1)/2)+possibilities[0]["tails"])][0]
        if int(choice) == 0:
            if possibilities[0]["cheater"] == True:
                possibilities.extend([{"heads":possibilities[0]["heads"]+1, "tails":possibilities[0]["tails"], "flips":possibilities[0]["flips"]-1, "cheater":True, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.75}, {"heads":possibilities[0]["heads"], "tails":possibilities[0]["tails"]+1, "flips":possibilities[0]["flips"]-1, "cheater":True, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.25}])
                possibilities.pop(0)
            elif possibilities[0]["cheater"] == False:
                possibilities.extend([{"heads":possibilities[0]["heads"]+1, "tails":possibilities[0]["tails"], "flips":possibilities[0]["flips"]-1, "cheater":False, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.5}, {"heads":possibilities[0]["heads"], "tails":possibilities[0]["tails"]+1, "flips":possibilities[0]["flips"]-1, "cheater":False, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.5}])
                possibilities.pop(0)
        elif int(choice) == 1:
            if possibilities[0]["cheater"] == False:
                possibilities.extend([{"heads":0, "tails":0, "flips":possibilities[0]["flips"]+15, "cheater":True, "points":possibilities[0]["points"]+1, "chance":possibilities[0]["chance"]*0.5}, {"heads":0, "tails":0, "flips":possibilities[0]["flips"]+15, "cheater":False, "points":possibilities[0]["points"]+1, "chance":possibilities[0]["chance"]*0.5}])
                possibilities.pop(0)
            elif possibilities[0]["cheater"] == True:
                possibilities.extend([{"heads":0, "tails":0, "flips":possibilities[0]["flips"]-30, "cheater":True, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.5}, {"heads":0, "tails":0, "flips":possibilities[0]["flips"]-30, "cheater":False, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.5}])
                possibilities.pop(0)
        elif int(choice) == 2:
            if possibilities[0]["cheater"] == True:
                possibilities.extend([{"heads":0, "tails":0, "flips":possibilities[0]["flips"]+15, "cheater":True, "points":possibilities[0]["points"]+1, "chance":possibilities[0]["chance"]*0.5}, {"heads":0, "tails":0, "flips":possibilities[0]["flips"]+15, "cheater":False, "points":possibilities[0]["points"]+1, "chance":possibilities[0]["chance"]*0.5}])
                possibilities.pop(0)
            elif possibilities[0]["cheater"] == False:
                possibilities.extend([{"heads":0, "tails":0, "flips":possibilities[0]["flips"]-30, "cheater":True, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.5}, {"heads":0, "tails":0, "flips":possibilities[0]["flips"]-30, "cheater":False, "points":possibilities[0]["points"], "chance":possibilities[0]["chance"]*0.5}])
                possibilities.pop(0)
        change = 0
        for i in range(1, 3):
            if possibilities[-i+change]["flips"] < 0 or possibilities[-i+change]["chance"] < 1e-6:
                dead_possibilities.append(possibilities[-i+change])
                possibilities.pop(-i+change)
                change =+ 1
        if len(possibilities) == 0:
            break
    average = 0
    possibilities.extend(dead_possibilities)
    for i in range(0, len(possibilities)):
        average += possibilities[i]["points"]*possibilities[i]["chance"]
    return average

    
generations = int(input("How many generations? - "))
prevscore = fitness(open(r'Primer\prevstrat.text').readlines())

for i in range(1, generations+1):
    strat = open(r'Primer\prevstrat.text').readlines()
    open(r'Primer\newstrat.text', 'w').write("")

    for x in range(0, len(strat)):
        if random.random() < 0.1:
            strat[x] = str(random.randrange(0, 3)) + "\n"

    for item in strat:
        open(r'Primer\newstrat.text', 'a').write(str(item))
    newscore = fitness(open(r'Primer\newstrat.text').readlines())
    if prevscore < newscore:
        shutil.copyfile(r'Primer\newstrat.text', r'Primer\prevstrat.text')
        prevscore = newscore
        print("Strat changed")
    else:
        print("Strat didn't change")
    print(str(i/generations))
    print(prevscore)
    print(newscore)
    print("")