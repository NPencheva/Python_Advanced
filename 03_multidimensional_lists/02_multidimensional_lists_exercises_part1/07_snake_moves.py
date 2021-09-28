from io import StringIO
import sys
from collections import deque

input1 = """5 6
SoftUni"""
input2 = """1 4
Python"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

n, m = [int(x) for x in input().split()]

string = deque(el for el in input())
new_matrix = []

for row_index in range(n):
    for col_index in range(m):
        new_matrix.append([])
        current_char = string.popleft()
        string.append(current_char)
        if row_index % 2 == 0:
            new_matrix[row_index].append(current_char)
        else:
            new_matrix[row_index].insert(0, current_char)

for row in new_matrix:
    print("".join(el for el in row))


