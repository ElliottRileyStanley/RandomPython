from itertools import permutations

solutions = []

for x in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10):
    if x[0] + x[1] + x[2] + x[3] == x[0] + x[4] + x[6] == x[3] + x[5] + x[9] == x[6] + x[7] + x[8] + x[9]:
        solutions.append(x)

max = 0
for solution in solutions:
    sum = solution[0] + solution[1] + solution[2] + solution[3]
    if sum <= max:
        max = sum
        print(str(sum) + " - " + str(solution))