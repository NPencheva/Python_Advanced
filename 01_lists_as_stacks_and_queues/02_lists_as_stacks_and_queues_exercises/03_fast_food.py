from io import StringIO
import sys
from collections import deque

input1 = """348
20 54 30 16 7 9"""
input2 = """499
57 45 62 70 33 90 88 76 100 50"""
sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

food_quantity = int(input())
orders = deque(map(int, input().split(" ")))

print(max(orders))

while orders:
    if food_quantity < orders[0]:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break
    else:
        current_order = orders.popleft()
        food_quantity -= current_order

if not orders:
    print("Orders complete")


