"""
"Primer's coin attempt 2" strat
[
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
"""


strategy = [
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class game:
    def __init__(self, cheater, heads, tails, chance):
        self.isCheater = cheater
        self.numHeads = heads
        self.numTails = tails
        self.percentChance = chance
        self.fitness = 0

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "Cheater-" + str(self.isCheater) + " H-" + str(self.numHeads) + " T-" + str(self.numTails) + " Chance-" + str(self.percentChance)
    
    # Equal if everything but percent chance is equal. Used to see if games can be combined.
    def __eq__(self, other):
        return self.isCheater == other.isCheater and self.numHeads == other.numHeads and self.numTails == other.numTails and self.fitness == 0 and other.fitness == 0
    
    def flip(self):
        if self.isCheater:
            return [
                game(True, self.numHeads+1, self.numTails, self.percentChance*.75), 
                game(True, self.numHeads, self.numTails+1, self.percentChance*.25)
                ]
        else:
            return [
                game(False, self.numHeads+1, self.numTails, self.percentChance*.5), 
                game(False, self.numHeads, self.numTails+1, self.percentChance*.5)
                ]

    def finish(self):
        global strategy
        if (strategy[self.numTails][self.numHeads] == 2 and self.isCheater == False) or (strategy[self.numTails][self.numHeads] == 1 and self.isCheater == True):
            self.fitness = -30 - self.numHeads - self.numTails
        else:
            self.fitness = 15 - self.numHeads - self.numTails




game_list = [game(True, 0, 0, 0.5), game(False, 0, 0, 0.5)]
results = []

while True:
    try:
        current_game = game_list.pop(0)
    except IndexError:
        break
    if strategy[current_game.numTails][current_game.numHeads] == 0:
        game_list += current_game.flip()
    else:
        current_game.finish()
        results.append(current_game)
    print(len(game_list))

averageGain = 0.0

for g in results:
    averageGain += g.fitness * g.percentChance

print(averageGain)