from io import StringIO
import sys

input1 = """SoftUni rocks"""
input2 = """Why do you like Python?"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

text = input()
elements_dict = {}

for index, value in enumerate(text):
    elements_dict[value] = text.count(value)

for key, value in sorted(elements_dict.items()):
    print(f"{key}: {value} time/s")



