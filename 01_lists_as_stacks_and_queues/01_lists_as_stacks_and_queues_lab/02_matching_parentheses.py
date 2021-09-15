from io import StringIO
import sys

input1 = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
input2 = "(2 + 3) - (2 + 3)"
sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

expression = list(input())
stack_opening = []

for index, value in enumerate(expression):
    if value == "(":
        stack_opening.append(index)
    elif value == ")":
        opening_index = stack_opening.pop()
        closing_index = index
        print("".join(expression[opening_index:closing_index + 1]))

