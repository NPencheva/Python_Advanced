from io import StringIO
import sys

input1 = """5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0"""
input2 = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22"""
input_test = """5
1 10 7 9 11
X 1 4 X 63
7 3 21 95 1
100000 B 73 4 9
1 1000 33 1 0"""


# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input_test)


# n, m = [int(x) for x in input().split()]
size = int(input())


def read_matrix():
    this_matrix = []

    for _ in range(size):
        row = [x for x in input().split(" ")]
        this_matrix.append(row)

    return this_matrix


matrix = read_matrix()


def bunny_position():
    b_row, b_col = 0, 0
    is_bunny = False

    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == "B":
                b_row, b_col = row_index, col_index
                is_bunny = True
                break
        if is_bunny:
            break

    return b_row, b_col


bunny_row, bunny_col = bunny_position()[0], bunny_position()[1]


def bunny_up(field, row, col):
    result = 0
    indices_list = []
    if row == 0:
        return result
    for r in range(row - 1, -1, -1):
        if field[r][col] == "X":
            break
        result += int(field[r][col])
        indices_list.append([r, col])
    dict_results["up"] = result
    dict_indices["up"] = indices_list
    return result


def bunny_down(field, row, col):
    result = 0
    indices_list = []
    if row == size - 1:
        return result
    for r in range(row + 1, size):
        if field[r][col] == "X":
            break
        result += int(field[r][col])
        indices_list.append([r, col])
    dict_results["down"] = result
    dict_indices["down"] = indices_list
    return result


def bunny_left(field, row, col):
    result = 0
    indices_list = []
    if col == 0:
        return result
    for c in range(col - 1, -1, -1):
        if field[row][c] == "X":
            break
        result += int(field[row][c])
        indices_list.append([row, c])
    dict_results["left"] = result
    dict_indices["left"] = indices_list
    return result


def bunny_right(field, row, col):
    result = 0
    indices_list = []
    if col == size - 1:
        return result
    for c in range(col + 1, size):
        if field[row][c] == "X":
            break
        result += int(field[row][c])
        indices_list.append([row, c])
    dict_results["right"] = result
    dict_indices["right"] = indices_list
    return result


def max_sum():
    greatest_sum = 0
    for key, value in dict_results.items():
        if value > greatest_sum:
            greatest_sum = value
    return greatest_sum


def max_indices():
    result = []
    for key, values in dict_indices.items():
        if key == max_path:
            result = [el for el in values]
    return result


dict_results = {}
dict_indices = {}
bunny_up(matrix, bunny_row, bunny_col)
bunny_down(matrix, bunny_row, bunny_col)
bunny_left(matrix, bunny_row, bunny_col)
bunny_right(matrix, bunny_row, bunny_col)


max_path = max(dict_results, key=dict_results.get)

print(max_path)

for item in max_indices():
    print(item)

print(max_sum())







