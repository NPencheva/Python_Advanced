from io import StringIO
import sys
from collections import deque
from math import floor

input1 = """6 3 - 2 1 * 5 /"""
input2 = """2 2 - 1 *"""
input3 = """10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


input_deque = deque(input().split())
numbers_deque = deque()
operators = ["*", "+", "-", "/"]

for i in input_deque:
    if i in operators:
        result = numbers_deque.popleft()
        while numbers_deque:
            current_number = numbers_deque.popleft()
            if i == "*":
                result = result * current_number
            elif i == "+":
                result = result + current_number
            elif i == "-":
                result = result - current_number
            elif i == "/":
                result = floor(result / current_number)
        numbers_deque.append(result)
    else:
        numbers_deque.append(int(i))

for el in numbers_deque:
    print(el)
