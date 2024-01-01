import json
import math
import random
import copy

bestbrain = json.loads(open(r'C:\Users\Ellio\OneDrive\Desktop\Python\Random\Primer\Neural Network\brain.json').read())

def sigmoid(value):
    return 1/(1+(math.exp(1)**(value*-1)))

def brainchoice(heads, tails, flips, brain):
    I1 = sigmoid(heads)
    I2 = sigmoid(tails)
    I3 = sigmoid(flips)
    for node in brain:
        vars()[node["name"]] = 0
        value = 0
        for connection in node["connections"]:
            value += vars()[connection]*node["connections"][connection]
        value = sigmoid(value)
        node["value"] = value
        vars()[node["name"]] = value
    AF = vars()["O1"]
    AC = vars()["O2"]
    F = vars()["O3"]
    if F >= max(AF, AC):
        return 0
    elif AF >= AC:
        return 1
    else:
        return 2
    
def fitness(brain):
    global possibilities
    possibilities = [{"heads":0, "tails":0, "flips":100, "cheater":True, "points":0, "chance":0.5},{"heads":0, "tails":0, "flips":100, "cheater":False, "points":0, "chance":0.5}]
    dead_possibilities = []
    while True:
        choice = brainchoice(possibilities[0]["heads"], possibilities[0]["tails"], possibilities[0]["flips"], brain)
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
            if possibilities[-i+change]["flips"] < 0 or possibilities[-i+change]["chance"] < 1e-6 or possibilities[-i+change]["points"] > 5000:
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

def generatebrains(bestbrain):
    changed_node = random.randint(0, len(bestbrain)-1)
    changed_connection = random.randint(0, len(bestbrain[changed_node]["connections"])-1)
    
    testbrains = []
    for value in range(-100, 101, 1):
        newbrain = copy.deepcopy(bestbrain)
        newbrain[changed_node]["connections"][list(newbrain[changed_node]["connections"].keys())[changed_connection]] = value/10
        testbrains.append(newbrain)
    return testbrains

testbrains = generatebrains(bestbrain)
bestscore = fitness(testbrains[0])
print(bestscore)
bestindex = 0
for index in range(1, len(testbrains)):
    currentscore = fitness(testbrains[index])
    if currentscore > bestscore:
        print("1")
        print(bestscore)
        bestscore = currentscore
        bestindex = index
    
print(testbrains[bestindex])