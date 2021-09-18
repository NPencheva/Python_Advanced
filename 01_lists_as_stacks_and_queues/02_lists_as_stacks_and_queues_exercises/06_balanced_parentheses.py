from io import StringIO
import sys

input1 = "{[()]}"
input2 = "{[(])}"
input3 = "{{[[(())]]}}"
input_test = "{}[]()"
# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
sys.stdin = StringIO(input_test)

sequence = list(input())

opening_paren = []

if len(sequence) % 2 != 0:
    print("NO")
else:
    for index, value in enumerate(sequence):
        if value == "{" or value == "[" or value == "(":
            opening_paren.append(value)
        else:
            if (value == "}" and opening_paren[-1] == "{") or (
                    value == "]" and opening_paren[-1] == "[") or (
                    value == ")" and opening_paren[-1] == "("):
                opening_paren.pop()
            else:
                print("NO")
                break
    if not opening_paren:
        print("YES")
