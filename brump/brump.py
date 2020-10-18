from bangtal import *
import random

# Player 1의 정보
player_one = [1, "spade", 13]

# Player 2의 정보
player_two = [2, "clover", 13]

one = random.randrange(0, 4)
while True:
    two = random.randrange(0, 4)
    if two != one:
        break

if one == 0:
    player_one[1] = "spade"
elif one == 1:
    player_one[1] = "clover"
elif one == 2:
    player_one[1] = "heart"
elif one == 3:
    player_one[1] = "diamond"

if two == 0:
    player_two[1] = "spade"
elif two == 1:
    player_two[1] = "clover"
elif two == 2:
    player_two[1] = "heart"
elif two == 3:
    player_two[1] = "diamond"

# Player 순서
player_turn = player_one

# Player 상태
state = 0

# 화면 상태
order = 0

# Player가 선택한 말
location = 0

# Player 1, Player 2 말 배치
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

# Black Joker 말 배치
black_joker = random.randrange(0, 13)
board[78 + black_joker][0] = 3
board[78 + black_joker][1] = 14
board[78 + black_joker][2] = 10

# Color Joker 말 배치 + Black Joker와 겹치지 않을 때까지 반복
while True:
    color_joker = random.randrange(0, 13)
    if black_joker != color_joker:
        break
board[78 + color_joker][0] = 4
board[78 + color_joker][1] = 14
board[78 + color_joker][2] = 10

# 게임 화면에 불필요한 요소 제거
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

# 장면 전환
background_start = Scene("START", "Images/board_start.png")
background_rule = Scene("RULE", "Images/board_rule.png")
background_game = Scene("BRUMP", "Images/board_game.png")
background_end = Scene("END", "Images/board_end.png")

background_zero = Object("Images/board_zero.png")
background_zero.locate(background_start, 0, 0)
background_zero.show()

for index in range(0, 169):
    if board[index][0] == 0:
        piece = Object("Images/cell.png")
        piece.locate(background_game, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 1:
        piece = Object("Images/" + player_one[1] + "_" + str(board[index][1]) + ".png")
        piece.locate(background_game, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 2:
        piece = Object("Images/" + player_two[1] + "_" + str(board[index][1]) + ".png")
        piece.locate(background_game, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 3:
        piece = Object("Images/joker_0.png")
        piece.locate(background_game, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()
    elif board[index][0] == 4:
        piece = Object("Images/joker_1.png")
        piece.locate(background_game, 290 + 54 * (index % 13), 658 - 54 * (index // 13))
        piece.show()

def onMouseAction_zero(x, y, action):
    global player_one, player_two, player_turn, state, order, location, board, background_game, background_start, background_rule, background_zero
    
    if order == 0:
        order += 1
        background_rule.enter()
        background_zero = Object("Images/board_zero.png")
        background_zero.locate(background_rule, 0, 0)
        background_zero.show()
        background_zero.onMouseAction = onMouseAction_zero
    elif order == 1:
        order += 1
        background_game.enter()
        background_zero = Object("Images/board_zero.png")
        background_zero.locate(background_game, 0, 0)
        background_zero.show()
        background_zero.onMouseAction = onMouseAction_zero
    elif order == 2:
        cell = ((x - 290) // 54) + (712 - y) // 54 * 13
        print("Player Number: " + str(board[cell][0]) + "   Card Number: " + str(board[cell][1]) + "   Card Attack: " + str(board[cell][2]))
    
        # 해당 차례의 플레이어가 말을 선택할 경우
        if board[cell][0] == player_turn[0] and state == 0:
            state = 1
            location = cell
        # 선택한 말이 1부터 10사이의 말일 경우 + 이동할 위치가 비어있는 공간, 적군, 아군일 경우
        elif (abs(cell - location) == 1 or abs(cell - location) == 13) and board[location][2] >= board[cell][2] and 1 <= board[location][1] <= 10 and state == 1:
            if board[cell][0] == 1:
                player_one[2] -= 1
            elif board[cell][0] == 2:
                player_two[2] -= 1

            board[cell][0] = board[location][0]
            board[cell][1] = board[location][1]
            board[cell][2] += board[location][2]
            board[location][0] = 0
            board[location][1] = 0
            board[location][2] = 0

            piece = Object("Images/cell.png")
            piece.locate(background_game, 290 + 54 * (location % 13), 658 - 54 * (location // 13))
            piece.show()
            piece = Object("Images/" + player_turn[1] + "_" + str(board[cell][1]) + ".png")
            piece.locate(background_game, 290 + 54 * (cell % 13), 658 - 54 * (cell // 13))
            piece.show()

            state = 0
            location = 0
            cell = 0
            if player_turn[0] == 1:
                player_turn = player_two
            else:
                player_turn = player_one

            background_zero = Object("Images/board_zero.png")
            background_zero.locate(background_game, 0, 0)
            background_zero.show()
            background_zero.onMouseAction = onMouseAction_zero
        # 선택한 말이 11부터 14사이의 말일 경우 + 이동할 위치가 비어있는 공간, 적군, 아군일 경우
        elif (abs(cell - location) == 1 or abs(cell - location) == 2 or abs(cell - location) == 13 or abs(cell - location) == 26) and board[location][2] >= board[cell][2] and 11 <= board[location][1] <= 14 and state == 1:
            if board[cell][0] == 1:
                player_one[2] -= 1
            elif board[cell][0] == 2:
                player_two[2] -= 1

            board[cell][0] = board[location][0]
            board[cell][1] = board[location][1]
            board[cell][2] += board[location][2]
            board[location][0] = 0
            board[location][1] = 0
            board[location][2] = 0

            piece = Object("Images/cell.png")
            piece.locate(background_game, 290 + 54 * (location % 13), 658 - 54 * (location // 13))
            piece.show()
            piece = Object("Images/" + player_turn[1] + "_" + str(board[cell][1]) + ".png")
            piece.locate(background_game, 290 + 54 * (cell % 13), 658 - 54 * (cell // 13))
            piece.show()

            state = 0
            location = 0
            cell = 0
            if player_turn[0] == 1:
                player_turn = player_two
            else:
                player_turn = player_one

            background_zero = Object("Images/board_zero.png")
            background_zero.locate(background_game, 0, 0)
            background_zero.show()
            background_zero.onMouseAction = onMouseAction_zero
        # 선택한 말이 1부터 10사이의 말일 경우 + 이동할 위치가 조커일 경우
        elif (abs(cell - location) == 1 or abs(cell - location) == 13) and board[cell][1] == 14 and (board[cell][0] == 3 or board[cell][0] == 4) and 1 <= board[location][1] <= 10 and state == 1:
            board[cell][0] = board[location][0]
            board[cell][1] = 14
            board[cell][2] += board[location][2]
            board[location][0] = 0
            board[location][1] = 0
            board[location][2] = 0

            piece = Object("Images/cell.png")
            piece.locate(background_game, 290 + 54 * (location % 13), 658 - 54 * (location // 13))
            piece.show()
            piece = Object("Images/" + player_turn[1] + "_" + str(board[cell][1]) + ".png")
            piece.locate(background_game, 290 + 54 * (cell % 13), 658 - 54 * (cell // 13))
            piece.show()

            state = 0
            location = 0
            cell = 0
            if player_turn[0] == 1:
                player_turn = player_two
            else:
                player_turn = player_one

            background_zero = Object("Images/board_zero.png")
            background_zero.locate(background_game, 0, 0)
            background_zero.show()
            background_zero.onMouseAction = onMouseAction_zero
        # 선택한 말이 11부터 14사이의 말일 경우 + 이동할 위치가 조커일 경우
        elif (abs(cell - location) == 1 or abs(cell - location) == 2 or abs(cell - location) == 13 or abs(cell - location) == 26) and board[cell][1] == 14 and (board[cell][0] == 3 or board[cell][0] == 4) and 11 <= board[location][1] <= 14 and state == 1:
            board[cell][0] = board[location][0]
            board[cell][1] = board[location][1]
            board[cell][2] += board[location][2]
            board[location][0] = 0
            board[location][1] = 0
            board[location][2] = 0

            piece = Object("Images/cell.png")
            piece.locate(background_game, 290 + 54 * (location % 13), 658 - 54 * (location // 13))
            piece.show()
            piece = Object("Images/" + player_turn[1] + "_" + str(board[cell][1]) + ".png")
            piece.locate(background_game, 290 + 54 * (cell % 13), 658 - 54 * (cell // 13))
            piece.show()

            state = 0
            location = 0
            cell = 0
            if player_turn[0] == 1:
                player_turn = player_two
            else:
                player_turn = player_one

            background_zero = Object("Images/board_zero.png")
            background_zero.locate(background_game, 0, 0)
            background_zero.show()
            background_zero.onMouseAction = onMouseAction_zero
        # 나머지의 경우 해당 차례의 플레이어는 말을 다시 선택
        else:
            state = 0
            location = 0
            cell = 0

            background_zero = Object("Images/board_zero.png")
            background_zero.locate(background_game, 0, 0)
            background_zero.show()
            background_zero.onMouseAction = onMouseAction_zero

        if player_one[2] == 0:
            order += 1
            background_end.enter()
            background_zero = Object("Images/board_zero.png")
            background_zero.locate(background_end, 0, 0)
            background_zero.show()
            background_zero.onMouseAction = onMouseAction_zero
        elif player_two[2] == 0:
            order += 1
            background_end.enter()
            background_zero = Object("Images/board_zero.png")
            background_zero.locate(background_end, 0, 0)
            background_zero.show()
            background_zero.onMouseAction = onMouseAction_zero
    elif order == 3:
        endGame()

background_zero.onMouseAction = onMouseAction_zero

startGame(background_start)
