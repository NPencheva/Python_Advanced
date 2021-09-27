from io import StringIO
import sys

input1 = """3
1, 2, 3
4, 5, 6
7, 8, 9"""
input2 = """..."""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

# n, m = [int(x) for x in input().split(", ")]
n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()

primary_diagonal = []
sum_primary = int()
secondary_diagonal = []
sum_secondary = int()

for index in range(n):
    sum_primary += matrix[index][index]
    primary_diagonal.append(matrix[index][index])

    sum_secondary += matrix[index][n - index - 1]
    secondary_diagonal.append(matrix[index][n - index - 1])

print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum_secondary}")
