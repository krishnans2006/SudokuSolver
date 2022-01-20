import time
from datetime import datetime

# board = [
#     [0, 0, 0, 7, 9, 0, 0, 5, 0],
#     [3, 5, 2, 0, 0, 8, 0, 4, 0],
#     [0, 0, 0, 0, 0, 0, 0, 8, 0],
#     [0, 1, 0, 0, 7, 0, 0, 0, 4],
#     [6, 0, 0, 3, 0, 1, 0, 0, 8],
#     [9, 0, 0, 0, 8, 0, 0, 1, 0],
#     [0, 2, 0, 0, 0, 0, 0, 0, 0],
#     [0, 4, 0, 5, 0, 0, 8, 9, 1],
#     [0, 8, 0, 0, 3, 7, 0, 0, 0]
# ]


def check_validity(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] != 0:
                validity = valid(bo, bo[i][j], (i, j))
                if not validity:
                    return False
    return True


def print_board(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                bo[i][j] = " "
        if i % 3 == 0:
            if i == 0:
                print(" ----------------------------------- ")
            else:
                print("| --------- | --------- | --------- |")

        for j in range(9):
            if j % 3 == 0:
                print("|", end="  ")

            if j == 8:
                print(bo[i][j], end="  |\n")
            else:
                print(str(bo[i][j]), end="  ")
            if bo[i][j] == " ":
                bo[i][j] = 0
    print(" ----------------------------------- ")


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j

    return None


def valid(bo, num, pos):
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(bo, disp=True):
    if disp:
        time.sleep(0.01)
        print_board(bo)
    empty = find_empty(bo)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo, disp):
                return True

            bo[row][col] = 0

    return False


def main():
    print("This is a Sudoku Solver coded in Python!")
    if True:  # FUTURE: Pygame support
        board = input("Would you like me to solve a default board instead of a new board? (Y/n) ")
        if "y" in board:
            board = [
                [0, 0, 0, 7, 9, 0, 0, 5, 0],
                [3, 5, 2, 0, 0, 8, 0, 4, 0],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [0, 1, 0, 0, 7, 0, 0, 0, 4],
                [6, 0, 0, 3, 0, 1, 0, 0, 8],
                [9, 0, 0, 0, 8, 0, 0, 1, 0],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 4, 0, 5, 0, 0, 8, 9, 1],
                [0, 8, 0, 0, 3, 7, 0, 0, 0]
            ]
        else:
            board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            for i in range(9):
                for j in range(9):
                    board[i][j] = "?"
                    print_board(board)
                    valid = False
                    while not valid:
                        value = input("Enter the number that belongs here, or 0 to indicate a blank space: ")
                        if value.isdecimal():
                            board[i][j] = int(value)
                            valid = True
        disp = input("Would you like me to show you my steps as I solve this board? (Will take much more time, Y/n) ")
        print("I am solving this board:")
        print_board(board)
        if check_validity(board):
            start = datetime.now()
            success = solve(board, disp=("y" in disp))
            print_board(board)
            end = datetime.now()
            if success:
                print(f"I have solved this board in {(end - start).seconds}.{(end - start).microseconds} seconds")
            else:
                print("I couldn't solve this!")
        else:
            print("Invalid Board!")


if __name__ == '__main__':
    main()
