from io import StringIO
import sys

input1 = """3 4
A B B D
E B B B
I J B B"""
input2 = """2 2
a b
c d"""
input3 = """5 4
A A B D
A A B B
I J B B
C C C G
C C K P"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

n, m = [int(x) for x in input().split()]
# n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [x for x in input().split()]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()

counter_2x2 = 0

for row_index in range(n - 1):
    for col_index in range(m - 1):
        if matrix[row_index][col_index] == \
                matrix[row_index][col_index + 1] == \
                matrix[row_index + 1][col_index] == \
                matrix[row_index + 1][col_index + 1]:
            counter_2x2 += 1

print(counter_2x2)
