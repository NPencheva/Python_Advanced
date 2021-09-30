from io import StringIO
import sys

input1 = """3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END"""
input2 = """4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

# n, m = [int(x) for x in input().split()]
n = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split()]
        this_matrix.append(row)

    return this_matrix


def check_is_valid(length, row_value, col_value):
    row_value = int(row_value)
    col_value = int(col_value)
    if row_value < 0 or col_value < 0 or row_value > length - 1 or col_value > length - 1:
        return False
    else:
        return True


matrix = read_matrix()

while True:
    command_line = input()
    if command_line == "END":
        break
    else:
        command, r, c, value = command_line.split()
        if check_is_valid(n, r, c) is False:
            print("Invalid coordinates")
        elif command == "Add":
            matrix[int(r)][int(c)] += int(value)
        elif command == "Subtract":
            matrix[int(r)][int(c)] -= int(value)

for row_ in matrix:
    print(" ".join(str(el) for el in row_))
