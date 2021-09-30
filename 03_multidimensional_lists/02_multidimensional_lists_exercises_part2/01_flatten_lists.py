# https://judge.softuni.org/Contests/3194
#
from io import StringIO
import sys

input1 = """1 2 3 |4 5 6 |  7  88"""
input2 = """7 | 4  5|1 0| 2 5 |3"""
input3 = """1| 4 5 6 7  |  8 9"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


string = [el for el in input().split("|")]

new_string = " ".join(el for el in string[::-1])

flattened_list = [el for el in new_string.split()]

print(" ".join(r for r in flattened_list))
