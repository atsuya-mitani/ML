import tkinter
import random
import matplotlib.pyplot as plt

PLAYER1_TURN = 0
PLAYER2_TURN = 1
MAX_MATCH = 1000


now_turn = 0
set = 1
set_score_Player1 = []

board = [[0 for i in range(3)] for j in range(3)]
player = ["NOBODY", "PLAYER1", "PLAYER2"]

record = []

def reset_board():
    global board, now_turn
    board = [[0 for i in range(3)] for j in range(3)]
    now_turn = 0

def check_win():
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            record.append(player[board[0][i]])
            reset_board()

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            record.append(player[board[i][0]])
            reset_board()


    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        record.append(player[board[0][0]])
        reset_board()

    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != 0:
        record.append(player[board[2][0]])
        reset_board()

    if board[0][0]!=0 and board[0][1]!=0 and board[0][2]!=0 and board[1][0]!=0 and board[1][1]!=0 and board[1][2]!=0 and board[2][0]!=0 and board[2][1]!=0 and board[2][2]!=0:
        record.append(player[0])
        reset_board()

def random_AI(player):
    global now_turn, board
    enemy_x = random.randint(0, 2)
    enemy_y = random.randint(0, 2)

    if board[enemy_y][enemy_x] == 0:
        board[enemy_y][enemy_x] = player
        now_turn = now_turn + 1

def main():
    global now_turn, record, set, set_score_Player1
    if now_turn%2 == PLAYER1_TURN:
        random_AI(1)
    if now_turn%2 == PLAYER2_TURN:
        random_AI(2)

    check_win()
    if len(record) >= MAX_MATCH:
        print("{}セット目(１セット１０００回)".format(set))
        print("PLAYER1の勝率"+str(record.count("PLAYER1")/len(record)))
        set_score_Player1.append(record.count("PLAYER1")/len(record))
        print("PLAYER2の勝率"+str(record.count("PLAYER2")/len(record)))
        print("引き分け率"+str(record.count("NOBODY")/len(record)))
        set += 1
        record = []

while True:
    main()
    if set == 100:
        plt.plot(set_score_Player1)
        plt.show()
        print("１００セット行ったので終了します。")
        break
