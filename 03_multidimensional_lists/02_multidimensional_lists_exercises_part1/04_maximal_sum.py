from io import StringIO
import sys

input1 = """4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4"""
input2 = """5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

n, m = [int(x) for x in input().split()]
# n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split()]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()

max_sum = int()
max_row = 0
max_col = 0

for row_index in range(n - 2):
    for col_index in range(m - 2):
        current_sum = matrix[row_index][col_index] + \
                      matrix[row_index][col_index + 1] + \
                      matrix[row_index][col_index + 2] + \
                      matrix[row_index + 1][col_index] + \
                      matrix[row_index + 1][col_index + 1] + \
                      matrix[row_index + 1][col_index + 2] + \
                      matrix[row_index + 2][col_index] + \
                      matrix[row_index + 2][col_index + 1] + \
                      matrix[row_index + 2][col_index + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_col = col_index

print(f"Sum = {max_sum}")
print(f"{matrix[max_row][max_col]} {matrix[max_row][max_col + 1]} {matrix[max_row][max_col + 2]}")
print(f"{matrix[max_row + 1][max_col]} {matrix[max_row + 1][max_col + 1]} {matrix[max_row + 1][max_col + 2]}")
print(f"{matrix[max_row + 2][max_col]} {matrix[max_row + 2][max_col + 1]} {matrix[max_row + 2][max_col + 2]}")

