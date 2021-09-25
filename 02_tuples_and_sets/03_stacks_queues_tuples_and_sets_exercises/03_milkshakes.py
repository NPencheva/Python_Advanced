from io import StringIO
import sys
from collections import deque

input1 = """20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

chocolate = [int(el) for el in input().split(", ")]
cups_of_milk = deque(int(el) for el in input().split(", "))

milkshakes = 0

while chocolate and cups_of_milk:
    current_chocolate = chocolate.pop()
    current_milk = cups_of_milk.popleft()
    if current_chocolate == current_milk:
        milkshakes += 1
        if milkshakes == 5:
            break
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_milk)
    elif current_milk <= 0:
        chocolate.append(current_chocolate)
    else:
        cups_of_milk.append(current_milk)
        chocolate.append(current_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(el) for el in chocolate)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(el) for el in cups_of_milk)}")
else:
    print("Milk: empty")
