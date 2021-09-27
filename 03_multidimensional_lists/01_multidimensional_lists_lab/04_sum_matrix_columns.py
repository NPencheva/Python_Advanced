from io import StringIO
import sys

input1 = """3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0"""
input2 = """3, 3
1 2 3
4 5 6
7 8 9"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

n, m = [int(x) for x in input().split(", ")]


def read_matrix():
    # n = int(input())
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split()]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()

rows = len(matrix)

for column_index in range(m):
    sum_columns = 0
    for row_index in range(n):
        sum_columns += matrix[row_index][column_index]
    print(sum_columns)
