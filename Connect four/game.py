def printboard(board):
    for row in range(0, len(board[0])):
        prints = ""
        for column in range(0, len(board)):
            prints += str(board[column][row]) + " "
        print(prints)


board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
winner = 0
player = 1

while winner == 0:
    choice = input("Choose a column player " + str(player) + "!")

    if choice.isnumeric() == False or int(choice) > len(board) or int(choice) < 1:
        print("invalid choice")