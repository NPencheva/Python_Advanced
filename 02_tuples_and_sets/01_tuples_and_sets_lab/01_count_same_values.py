# https://judge.softuni.org/Contests/1832

from io import StringIO
import sys

input1 = "-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3"
input2 = "2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3"
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

# variant 1
#
# numbers = [float(el) for el in input().split()]
#
# numbers_counter = {}
#
# for n in numbers:
#     if n not in numbers_counter:
#         numbers_counter[n] = 1
#     else:
#         numbers_counter[n] += 1
#
# for key, value in numbers_counter.items():
#     print(f"{key:.1f} - {value} times")

# -------------------------------------------------------------
# variant 2:

numbers = tuple([float(el) for el in input().split()])

uniques = []

for n in numbers:
    if n not in uniques:
        uniques.append(n)
        print(f"{n} - {numbers.count(n)} times")
