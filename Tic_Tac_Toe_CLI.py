def create_board():
    return [[" ", " ", " " ], [" ", " ", " " ], [" ", " ", " " ]]

def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")

def gamePlay():
    ex_b = [["1", "2", "3" ], ["4", "5", "6" ], ["7", "8", "9" ]]
    gameIsOver = False
    player = 0 #calculates the player
    board = create_board()
    while gameIsOver == False:
        if player % 2 == 0:
            print_board(ex_b)
            p1 = int(input("Player 1; This enter the number coresponding to the position you want to play: "))
            row, col = divmod(p1 - 1, 3)
            if board[row][col] == " ":
                board[row][col] = "✖️"
                player += 1
            else:
                print("Invalid input, try again")
        elif player % 2 != 0:
            print_board(ex_b)
            p2 = int(input("Player 2; This enter the number coresponding to the position you want to play: "))
            row, col = divmod(p2 - 1, 3)
            if board[row][col] == " ":
                board[row][col] = "⭕"
                player += 1
            else:
                print("Invalid input, try again")
        print_board(board)

        count_emp = 0
        for i in range(3):
            if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
                if player % 2 == 0:
                    print("Player 2 Win")
                else:
                    print("Player 1 Win")
                gameIsOver = True
            elif board[0][i] != " " and board[0][i] == board[1][i] == board[2][i]:
                if player % 2 == 0:
                    print("Player 2 Win")
                else:
                    print("Player 1 Win")
                gameIsOver = True
            for j in range(3):
                if board[i][j] == " ":
                    count_emp += 1
                    
        if count_emp == 0 and gameIsOver == False:
            print("Draw")
            gameIsOver = True

        if board[1][1] != " " and (board[1][1] == board[0][0] == board[2][2] or board[1][1] == board[0][2] == board[2][0]):
            if player % 2 == 0:
                print("Player 2 Win")
            else:
                print("Player 1 Win")
            gameIsOver = True

gamePlay()