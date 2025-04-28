import random
import copy

def printBoard(board):
    for x in range(len(board)):
        row = ""
        for y in range(len(board[0])):
            row += str(board[x][y]).replace("0", "-").replace("1", "O") + " "
        print(row)

def randomBoard(boardWidth, boardHeight, shipLengths):
    board = [[0 for _ in range(boardWidth)] for _ in range(boardHeight)]
    for shipLength in shipLengths:
        doesFit = False

        while not doesFit:
            newBoard = copy.deepcopy(board)
            rotation = random.randint(0, 1)
            if rotation == 0:
                # horizontal
                xStart = random.randint(0, boardWidth - shipLength)
                yStart = random.randint(0, boardHeight - 1)
                # check if all positions are free
                fits = True
                for x in range(xStart, xStart + shipLength):
                    if board[yStart][x] == 1:
                        fits = False
                        break
                if fits:
                    for x in range(xStart, xStart + shipLength):
                        newBoard[yStart][x] = 1
                    doesFit = True
            else:
                # vertical
                xStart = random.randint(0, boardWidth - 1)
                yStart = random.randint(0, boardHeight - shipLength)
                fits = True
                for y in range(yStart, yStart + shipLength):
                    if board[y][xStart] == 1:
                        fits = False
                        break
                if fits:
                    for y in range(yStart, yStart + shipLength):
                        newBoard[y][xStart] = 1
                    doesFit = True

        board = newBoard

    printBoard(board)


print("Please input the width and height of the board that you want to randomly place ships on.")
while True:
    width = input("Width of board - ")
    if width.isdigit() and int(width) > 0:
        boardWidth = int(width)
        break
    else:
        print("Please input an integer")

while True:
    height = input("Height of board - ")
    if height.isdigit() and int(height) > 0:
        boardHeight = int(height)
        break
    else:
        print("Please input an integer")

print("Please input the lengths of the ships you want to place. When done, input \"done\"")
shipLengths = []
while True:
    length = input("Length - ")
    if length.isdigit():
        shipLengths.append(int(length))
    elif length.lower() == "done":
        break
    else:
        print("Please input an integer. If done, input \"done\"")
        continue

if sum(shipLengths) > boardWidth * boardHeight:
    print("Impossible to place all ships, please try again")
else:
    print()
    print("Here's your board!")
    randomBoard(boardWidth, boardHeight, shipLengths)