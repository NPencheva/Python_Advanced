from io import StringIO
import sys

input1 = """3
ABC
DEF
X!@
!"""
input2 = """4
asdd
xczc
qwee
qefw
4"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

# n, m = [int(x) for x in input().split(", ")]
n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [x for x in input()]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()
symbol = input()

is_symbol = False
r = int()
c = int()

for row_index in range(n):
    if is_symbol:
        break
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            is_symbol = True
            r = row_index
            c = col_index
            break

if is_symbol:
    print((r, c))
else:
    print(f"{symbol} does not occur in the matrix")