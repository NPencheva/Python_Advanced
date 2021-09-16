from io import StringIO
import sys
from collections import deque

input1 = """Tracy Emily Daniel
2"""
input2 = """George Peter Michael William Thomas
10"""
input3 = """George Peter Michael William Thomas
1"""
# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)


kids = deque(input().split(" "))
step = int(input())
counter = 0

while kids:

    if len(kids) == 1:
        print(f"Last is {kids[0]}")
        break
    else:
        counter += 1
        if counter == step:
            popped_kid = kids.popleft()
            print(f"Removed {popped_kid}")
            counter = 0
        else:
            kids.append(kids.popleft())
