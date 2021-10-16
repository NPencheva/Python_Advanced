from io import StringIO
import sys

input1 = """5 
0K0K0
K000K
00K00
K000K
0K0K0"""
input2 = """2
KK
KK"""
input3 = """8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

# n, m = [int(x) for x in input().split()]
size = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row = [x for x in input()]
        this_matrix.append(row)

    return this_matrix


def is_knight_at_position(board, row, col):
    board_size = len(board)
    if row < 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == "K"


def count_affected_knights(board, row, col):
    result = 0
    if is_knight_at_position(board, row - 1, col - 2):
        result += 1
    if is_knight_at_position(board, row - 1, col + 2):
        result += 1
    if is_knight_at_position(board, row + 1, col - 2):
        result += 1
    if is_knight_at_position(board, row + 1, col + 2):
        result += 1
    if is_knight_at_position(board, row - 2, col - 1):
        result += 1
    if is_knight_at_position(board, row - 2, col + 1):
        result += 1
    if is_knight_at_position(board, row + 2, col - 1):
        result += 1
    if is_knight_at_position(board, row + 2, col + 1):
        result += 1
    return result


matrix = read_matrix()

removed_knights = 0

while True:
    max_count, k_row, k_col = 0, 0, 0
    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == "0":
                continue
            count = count_affected_knights(matrix, row_index, col_index)
            if count > max_count:
                max_count, k_row, k_col = count, row_index, col_index
    if max_count == 0:
        break
    matrix[k_row][k_col] = "0"
    removed_knights += 1

print(removed_knights)


