from io import StringIO
import sys

input1 = """3
11 2 4
4 5 6
10 8 -12"""
input2 = """3
1 2 3
4 5 6
7 8 9"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

# n, m = [int(x) for x in input().split(", ")]
n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split()]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()

sum_diagonal = 0

for index in range(n):
    sum_diagonal += matrix[index][index]

print(sum_diagonal)
