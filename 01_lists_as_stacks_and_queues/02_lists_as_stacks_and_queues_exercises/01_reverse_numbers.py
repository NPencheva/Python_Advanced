# https://judge.softuni.org/Contests/1831

from io import StringIO
import sys

input1 = "1 2 3 4 5"
input2 = "1"
# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

stack = input().split(" ")
reverse_stack = []

for i in range(len(stack)):
    reverse_stack.append(stack.pop())

print(" ".join(reverse_stack))

