from bangtal import *
import random

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

background1 = Scene("PLAYER 1", "Images/board_1.png")
background2 = Scene("PLAYER 2", "Images/board_1.png")

player_one = [1, "spade"]
player_two = [2, "clover"]
player_turn = player_one
state = 0
location = 0

board = [[1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 11, 5], [1, 13, 10], [1, 12, 10], [1, 6, 1], [1, 7, 1], [1, 8, 1], [1, 9, 1], [1, 10, 1], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
         [2, 10, 1], [2, 9, 1], [2, 8, 1], [2, 7, 1], [2, 6, 1], [2, 12, 10], [2, 13, 10], [2, 11, 5], [2, 5, 1], [2, 4, 1], [2, 3, 1], [2, 2, 1], [2, 1, 1]]

black_joker = random.randrange(0, 13)
board[78 + black_joker][0] = 3
board[78 + black_joker][1] = 14
board[78 + black_joker][2] = 10

while True:
    color_joker = random.randrange(0, 13)
    if black_joker != color_joker:
        break
board[78 + color_joker][0] = 4
board[78 + color_joker][1] = 14
board[78 + color_joker][2] = 10

for index in range(0, 169):
    if board[index][0] == 0:
        piece = Object("Images/cell.png")
        piece.locate(background1, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 1:
        piece = Object("Images/" + player_one[1] + "_" + str(board[index][1]) + ".png")
        piece.locate(background1, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 2:
        piece = Object("Images/" + player_two[1] + "_" + str(board[index][1]) + ".png")
        piece.locate(background1, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 3:
        piece = Object("Images/joker_0.png")
        piece.locate(background1, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 4:
        piece = Object("Images/joker_1.png")
        piece.locate(background1, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()

background0 = Object("Images/board_0.png")
background0.locate(background1, 0, 0)
background0.show()
    
def onMouseAction_board(x, y, action):
    global player_one, player_two, player_turn, state, location, board, background0
    cell = ((x - 290) // 54) + (712 - y) // 54 * 13
    print(board[cell][0], board[cell][1], board[cell][2])
    
    if board[cell][0] == player_turn[0] and state == 0:
        state = 1
        location = cell
    elif (abs(cell - location) == 1 or abs(cell - location) == 13) and board[location][2] >= board[cell][2] and state == 1:
        board[cell][0] = board[location][0]
        board[cell][1] = board[location][1]
        board[cell][2] += board[location][2]
        board[location][0] = 0
        board[location][1] = 0
        board[location][2] = 0

        piece = Object("Images/cell.png")
        piece.locate(background1, 290 + 54 * (location % 13), 658 - 54 * (location // 13))
        piece.show()
        piece = Object("Images/" + player_turn[1] + "_" + str(board[cell][1]) + ".png")
        piece.locate(background1, 290 + 54 * (cell % 13), 658 - 54 * (cell // 13))
        piece.show()

        state = 0
        if player_turn[0] == 1:
            player_turn = player_two
        else:
            player_turn = player_one

        background0 = Object("Images/board_0.png")
        background0.locate(background1, 0, 0)
        background0.show()
        background0.onMouseAction = onMouseAction_board
    elif (abs(cell - location) == 1 or abs(cell - location) == 13) and board[cell][1] == 14 and (board[cell][0] == 3 or board[cell][0] == 4) and state == 1:
        board[cell][0] = board[location][0]
        if board[location][1] != 11 and board[location][1] != 12 and board[location][1] != 13:
            board[cell][1] = 14
        else:
            board[cell][1] = board[location][1]
        board[cell][2] += board[location][2]
        board[location][0] = 0
        board[location][1] = 0
        board[location][2] = 0

        piece = Object("Images/cell.png")
        piece.locate(background1, 290 + 54 * (location % 13), 658 - 54 * (location // 13))
        piece.show()
        piece = Object("Images/" + player_turn[1] + "_" + str(board[cell][1]) + ".png")
        piece.locate(background1, 290 + 54 * (cell % 13), 658 - 54 * (cell // 13))
        piece.show()

        state = 0
        if player_turn[0] == 1:
            player_turn = player_two
        else:
            player_turn = player_one

        background0 = Object("Images/board_0.png")
        background0.locate(background1, 0, 0)
        background0.show()
        background0.onMouseAction = onMouseAction_board
    else:
        state = 0
background0.onMouseAction = onMouseAction_board

startGame(background1)
