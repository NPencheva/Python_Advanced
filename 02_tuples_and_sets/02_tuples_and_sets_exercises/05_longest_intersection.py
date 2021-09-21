from io import StringIO
import sys

input1 = """3
0,3-1,2
2,10-3,5
6,15-3,10"""
input2 = """5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

number = int(input())

longest_length = 0
longest_inters = set()

for n in range(number):
    range1, range2 = input().split("-")

    first_start, first_end = (int(el) for el in (range1.split(",")))
    second_start, second_end = (int(el) for el in (range2.split(",")))

    set1 = set(el for el in range(first_start, first_end + 1))
    set2 = set(el for el in range(second_start, second_end + 1))
    length_inters = len(set1.intersection(set2))
    inters = set1.intersection(set2)

    if len(set1.intersection(set2)) > longest_length:
        longest_length = length_inters
        longest_inters = inters

print(f"Longest intersection is {list(longest_inters)} with length {longest_length}")
