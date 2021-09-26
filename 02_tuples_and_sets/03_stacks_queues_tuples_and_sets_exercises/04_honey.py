from io import StringIO
import sys
from collections import deque

input1 = """20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /"""
input2 = """30
15 9 5 150 8
* + + * -"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

bees = deque(int(el) for el in input().split())
nectar = [int(el) for el in input().split()]
symbols = deque(input().split())

total_honey = 0

# def symbol_operations(num1, num2, operation):
#     result = None
#     if operation == "*":
#         result = num1 * num2
#     elif operation == "+":
#         result = num1 + num2
#     elif operation == "-":
#         result = num1 - num2
#     elif operation == "/":
#         if num2 != 0:
#             result = num1 / num2
#
#     return abs(result)


while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        # total_honey += symbol_operations(current_bee, current_nectar, current_symbol)
        if current_symbol == "*":
            total_honey += abs(current_bee * current_nectar)
        elif current_symbol == "+":
            total_honey += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            total_honey += abs(current_bee - current_nectar)
        elif current_symbol == "/":
            if current_nectar != 0:
                total_honey += abs(current_bee / current_nectar)

    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(el) for el in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(el) for el in nectar)}")
