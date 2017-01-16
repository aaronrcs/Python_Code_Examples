#This is Battleship againist the computer! You have 6 guesses to sink the computer's battleship!


from random import randint

board = []

#Create board with "O" (Big O's)
for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#ship_row and ship_col have random row and column number
ship_row = random_row(board)
ship_col = random_col(board)

#This loop will keep going as long as it has not reached 6 guesses
for turn in range(6):

    # Gets the users guess of a row and column
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    #This else statement block checks for any errors
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            #sets an "X" to the row and column in the board when a guess is incorrect
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 5:
            print("Game Over! Try Again")

        # This print statement keeps track of the turns the user is on!
        print("Turn", turn + 1)
        print("Current progress...")
        print_board(board)