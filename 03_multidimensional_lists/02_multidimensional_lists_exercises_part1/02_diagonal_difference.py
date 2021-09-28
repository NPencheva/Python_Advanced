from io import StringIO
import sys

input1 = """3
11 2 4
4 5 6
10 8 -12"""
input2 = """4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14"""

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

sum_primary = int()
sum_secondary = int()

for index in range(n):
    sum_primary += matrix[index][index]
    sum_secondary += matrix[index][n - index - 1]

sum_difference = abs(sum_primary - sum_secondary)

print(sum_difference)
