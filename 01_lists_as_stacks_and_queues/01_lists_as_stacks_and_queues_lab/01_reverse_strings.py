from io import StringIO
import sys

input1 = "I Love Python"
input2 = "Stacks and Queues"
sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


initial_string = list(input())
reversed_string_list = []

for ch in range(len(initial_string)):
    popped_ch = initial_string.pop()
    reversed_string_list.append(popped_ch)

print("".join(reversed_string_list))
