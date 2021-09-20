from io import StringIO
import sys

input1 = """4 3
1
3
5
7
3
4
5"""
input2 = """2 2
1
3
1
5"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

len_set1, len_set2 = (int(el) for el in input().split(" "))

set1 = set()
set2 = set()

for n in range(len_set1 + len_set2):
    number = int(input())
    if n < len_set1:
        set1.add(number)
    else:
        set2.add(number)

repeating = set1.intersection(set2)

for el in repeating:
    print(el)
