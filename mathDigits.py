from itertools import permutations

def boardString(board):
    return str(board[0]) + " " + str(board[1]) + " " + str(board[2]) + " " + str(board[3]) + "\n" + str(board[4]) + "     " + str(board[5]) + "\n" + str(board[6]) + " " + str(board[7]) + " " + str(board[8]) + " " + str(board[9])



solutions = []

print("All solutions - ")
for x in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10):
    sum = x[0] + x[1] + x[2] + x[3]
    if sum == x[0] + x[4] + x[6] == x[3] + x[5] + x[9] == x[6] + x[7] + x[8] + x[9]:
        solutions.append(x)
        print(str(sum) + " - " + str(x))
print("\n\n\n")

print("Number of solutions - " + str(len(solutions)))

max = 0
min = 100
maxSolution = []
minSolution = []
numOfMax = 0
numOfMin = 0
for solution in solutions:
    sum = solution[0] + solution[1] + solution[2] + solution[3]

    if sum > max:
        max = sum
        maxSolution = solution
        numOfMax = 1
    elif sum == max:
        numOfMax += 1
    
    if sum < min:
        min = sum
        minSolution = solution
        numOfMin = 1
    elif sum == min:
        numOfMin += 1
    

print("Biggest solution is a sum of " + str(max) + ". There are " + str(numOfMax) + " solutions with that sum" + ". \nExample - \n" + boardString(maxSolution))
print("\n")
print("Smallest solution is a sum of " + str(min)+ ". There are " + str(numOfMin) + " solutions with that sum" + ". \nExample - \n" + boardString(minSolution))
