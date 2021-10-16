from io import StringIO
import sys

input1 = """5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left"""
input2 = """7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)


# n, m = [int(x) for x in input().split()]
size = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row = [x for x in input().split(" ")]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()


def alice_position():
    a_row, a_col = 0, 0
    is_alice = False

    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == "A":
                a_row, a_col = row_index, col_index
                is_alice = True
                break
        if is_alice:
            break

    return a_row, a_col


alice_row, alice_col = alice_position()[0], alice_position()[1]
teabags_collected = 0

command = input()

while True:
    matrix[alice_row][alice_col] = "*"
    if command == "up":
        new_row = alice_row - 1
        new_col = alice_col
        if new_row < 0:
            print("Alice didn't make it to the tea party.")
            break
        new_position = matrix[new_row][new_col]
        if new_position == "R":
            matrix[new_row][new_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        elif new_position != "." and new_position != "*":
            teabags_collected += int(new_position)
        matrix[new_row][new_col] = "*"
        alice_row = new_row
        alice_col = new_col

    elif command == "down":
        new_row = alice_row + 1
        new_col = alice_col
        if new_row >= size:
            print("Alice didn't make it to the tea party.")
            break
        new_position = matrix[new_row][new_col]
        if new_position == "R":
            matrix[new_row][new_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        elif new_position != "." and new_position != "*":
            teabags_collected += int(new_position)
        matrix[new_row][new_col] = "*"
        alice_row = new_row
        alice_col = new_col

    elif command == "left":
        new_row = alice_row
        new_col = alice_col - 1
        if new_col < 0:
            print("Alice didn't make it to the tea party.")
            break
        new_position = matrix[new_row][new_col]
        if new_position == "R":
            matrix[new_row][new_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        elif new_position != "." and new_position != "*":
            teabags_collected += int(new_position)
        matrix[new_row][new_col] = "*"
        alice_row = new_row
        alice_col = new_col

    elif command == "right":
        new_row = alice_row
        new_col = alice_col + 1
        if new_col >= size:
            print("Alice didn't make it to the tea party.")
            break
        new_position = matrix[new_row][new_col]
        if new_position == "R":
            matrix[new_row][new_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        elif new_position != "." and new_position != "*":
            teabags_collected += int(new_position)
        matrix[new_row][new_col] = "*"
        alice_row = new_row
        alice_col = new_col

    if teabags_collected >= 10:
        print("She did it! She went to the party.")
        break

    command = input()

for line in matrix:
    print(" ".join(line))
