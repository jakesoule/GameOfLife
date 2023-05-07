import random
import copy
import os
import time

def dead_state(width: int, height: int) -> list:
    gameBoard = []
    for i in range(height):
        gameBoard.append([])
        for j in range(width):
            gameBoard[i].append(0)
    return gameBoard


def random_state(width: int, height: int) -> list:
    state = dead_state(width, height)

    for i in range(width):
        for j in range(height):
            random_number = random.random()
            if random_number >= 0.99:
                state[j][i] = 1
            else:
                state[j][i] = 0
    return state


def render(state: list) -> None:
    width = len(state[0])
    height = len(state)

    for i in range(height):
        print("|", end='')
        for j in range(width):
            if state[i][j] == 1:
                print("#", end='')
            else:
                print(" ", end='')
        print("|")


def count_alive_neighbours(row: int, col: int, state: list) -> int:
    amount = 0

    if row == 0 and col == 0:
        amount = state[0][1] + state[1][0] + state[1][1]

    elif row == 0 and col == len(state[0])-1:
        amount = state[0][col-1] + state[1][col-1] + state[1][col]

    elif row == len(state)-1 and col == 0:
        amount = state[row-1][0] + state[row-1][1] + state[row][1]

    elif row == len(state)-1 and col == len(state[0])-1:
        amount = state[row-1][col] + state[row][col-1] + state[row-1][col-1]

    elif row == 0:
        amount = state[0][col-1] + state[0][col+1] + state[1][col-1] + state[1][col] + state[1][col+1]

    elif row == len(state)-1:
        amount = state[row][col-1] + state[row][col+1] + state[row-1][col-1] + state[row-1][col] + state[row-1][col+1]

    elif col == 0:
        amount = state[row-1][0] + state[row+1][0] + state[row-1][1] + state[row][1] + state[row+1][1] 

    elif col == len(state[0])-1:
        amount = state[row-1][col] + state[row+1][col] + state[row-1][col-1] + state[row][col-1] + state[row+1][col-1]

    else:
        amount = state[row-1][col-1] + state[row-1][col-1] + state[row-1][col-1] + state[row][col] + state[row][col] + state[row+1][col+1] + state[row+1][col+1] + state[row+1][col+1]   
    return amount


def next_board_state(state: list) -> list:
    init_state = copy.deepcopy(state)

    for i in range(len(state)):
        for j in range(len(state[0])):
            alive_neighbours = count_alive_neighbours(i, j, init_state)

            if init_state[i][j] == 1:
                if alive_neighbours == 0 or alive_neighbours == 1:
                    state[i][j] = 0
                elif alive_neighbours == 2 or alive_neighbours == 3:
                    state[i][j] = 1
                elif alive_neighbours > 3: 
                    state[i][j] = 0

            elif init_state[i][j] == 0:
                if alive_neighbours == 3:
                    state[i][j] = 1
    return state

clear = lambda: os.system('cls')


if __name__ == '__main__':
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    init_state = random_state(width, height)

    while True:
        clear()
        render(next_board_state(init_state))
        time.sleep(1)