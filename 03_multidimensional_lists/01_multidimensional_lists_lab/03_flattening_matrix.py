from io import StringIO
import sys

input1 = """2
1, 2, 3
4, 5, 6"""
input2 = """3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


def read_matrix():
    # n, m = [int(x) for x in input().split(", ")]
    n = int(input())
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()

rows = len(matrix)
flattened_matrix = []

for r in matrix:
    [flattened_matrix.append(el) for el in r]

print(flattened_matrix)
