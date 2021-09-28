from io import StringIO
import sys

input1 = """2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END"""
input2 = """1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

n, m = [int(x) for x in input().split()]
# n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [x for x in input().split()]
        this_matrix.append(row)

    return this_matrix


def is_valid_input(r, c, rows, cols):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return False
    return True


matrix = read_matrix()

while True:
    command_line = input()
    if command_line == "END":
        break

    else:
        command = command_line.split()

        if command[0] != "swap" or len(command) != 5:
            print("Invalid input!")
            continue

        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if not is_valid_input(row1, col1, n, m) or not is_valid_input(row2, col2, n, m):
        # if row1 >= n or row2 >= n or col1 >= m or col2 >= m or (row1 or row2 or col1 or col2) < 0:
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            for row_index in matrix:
                print(" ".join(str(el) for el in row_index))
