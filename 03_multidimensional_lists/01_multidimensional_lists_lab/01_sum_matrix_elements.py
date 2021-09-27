# https://judge.softuni.org/Contests/1834
#
from io import StringIO
import sys

input1 = """3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0"""
input2 = """..."""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


def read_matrix():
    n, m = [int(x) for x in input().split(", ")]
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()
summed_numbers = 0

for row_index in range(len(matrix)):
    for el in matrix[row_index]:
        summed_numbers += el

print(summed_numbers)
print(matrix)
