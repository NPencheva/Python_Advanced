from io import StringIO
import sys
from collections import deque

input1 = """2
Peter
Amy
Start
2
refill 1
1
End"""
input2 = """10
Peter
George
Amy
Alice
Start
2
3
3
3
End"""
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

people = deque()

starting_quantity = int(input())
liters_left = starting_quantity

while True:
    command = input()
    if command == "Start":
        break
    else:
        people.append(command)

while True:
    command_new = input()
    if command_new == "End":
        break
    elif command_new.startswith("refill"):
        to_refill = command_new.split(" ")
        liters_left += int(to_refill[1])
    else:
        liters_needed = int(command_new)
        if liters_needed <= liters_left:
            liters_left -= liters_needed
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")

print(f"{liters_left} liters left")
