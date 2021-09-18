from io import StringIO
import sys
from collections import deque

input1 = """5 4 8 6 3 8 7 7 9
16"""
input2 = """1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20"""
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

clothes_in_box = list(map(int, input().split(" ")))     #stack
# clothes_in_box = [int(el) for el in input().split(" ")] #stack
rack_capacity = int(input())
filled_capacity = 0
racks_counter = 0

while clothes_in_box:
    current_clothe = clothes_in_box[-1]
    if filled_capacity + current_clothe < rack_capacity:
        filled_capacity += current_clothe
        clothes_in_box.pop()
        if racks_counter == 0:
            racks_counter += 1
    elif filled_capacity + current_clothe == rack_capacity:
        clothes_in_box.pop()
        if clothes_in_box:
            filled_capacity = 0
            racks_counter += 1
    elif filled_capacity + current_clothe > rack_capacity:
        filled_capacity = clothes_in_box.pop()
        racks_counter += 1

print(racks_counter)