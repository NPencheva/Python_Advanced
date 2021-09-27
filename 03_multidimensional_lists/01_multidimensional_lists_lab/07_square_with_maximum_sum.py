from io import StringIO
import sys

input1 = """3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0"""
input2 = """2, 4
10, 11, 12, 13
14, 15, 16, 17"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

n, m = [int(x) for x in input().split(", ")]


# n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()

max_sum = int()
max_row = 0
max_col = 0

for row_index in range(n - 1):
    for col_index in range(m - 1):
        current_sum = matrix[row_index][col_index] + \
                      matrix[row_index][col_index + 1] + \
                      matrix[row_index + 1][col_index] + \
                      matrix[row_index + 1][col_index + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_col = col_index

print(f"{matrix[max_row][max_col]} {matrix[max_row][max_col + 1]}")
print(f"{matrix[max_row + 1][max_col]} {matrix[max_row + 1][max_col + 1]}")
print(max_sum)
