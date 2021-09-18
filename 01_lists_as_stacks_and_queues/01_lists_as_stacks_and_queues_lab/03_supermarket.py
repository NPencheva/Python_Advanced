from io import StringIO
import sys
from collections import deque

input1 = """George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End"""
input2 = """Anna
Emma
Alexander
End"""
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

queue = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        for i in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(command)
