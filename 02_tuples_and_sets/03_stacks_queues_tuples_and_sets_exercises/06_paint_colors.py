from io import StringIO
import sys
from collections import deque

input1 = """d yel blu e low redd"""
input2 = """r ue nge ora bl ed"""
input3 = """re ple blu pop e pur d"""
input_test = """re yellow bye"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)
# sys.stdin = StringIO(input_test)

colour_parts = deque(el for el in input().split())

colours = ["red", "yellow", "blue", "orange", "purple", "green"]
obtained_colours = []

while colour_parts:
    if len(colour_parts) == 1:
        current_colour = colour_parts.pop()
        if current_colour in colours:
            obtained_colours.append(current_colour)
    else:
        left_substring = colour_parts.popleft()
        right_substring = colour_parts.pop()
        current_colour_l = left_substring + right_substring
        current_colour_r = right_substring + left_substring
        if current_colour_l in colours:
            obtained_colours.append(current_colour_l)
        elif current_colour_r in colours:
            obtained_colours.append(current_colour_r)
        else:
            left_substring = left_substring[:-1]
            right_substring = right_substring[:-1]
            if left_substring:
                colour_parts.insert(len(colour_parts) // 2, left_substring)
            if right_substring:
                colour_parts.insert(len(colour_parts) // 2, right_substring)

if "orange" in obtained_colours and ("red" not in obtained_colours or "yellow" not in obtained_colours):
    obtained_colours.remove("orange")
if "purple" in obtained_colours and ("red" not in obtained_colours or "blue" not in obtained_colours):
    obtained_colours.remove("purple")
if "green" in obtained_colours and ("yellow" not in obtained_colours or "blue" not in obtained_colours):
    obtained_colours.remove("green")

print(obtained_colours)
