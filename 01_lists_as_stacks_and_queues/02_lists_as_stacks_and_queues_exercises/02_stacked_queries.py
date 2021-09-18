from io import StringIO
import sys

input1 = """9
1 97
2
1 20
2
1 26
1 20
3
1 91
4"""
input2 = """10
2
1 47
1 66
1 32
4
3
1 25
1 16
1 8
4"""
sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

number = int(input())
stack = []

for n in range(number):
    command_line = input().split()
    command = command_line[0]
    if command == "1":
        stack.append(int(command_line[1]))
    else:
        if stack:
            if command == "2":
                stack.pop()
            elif command == "3":
                print(max(stack))
            elif command == "4":
                print(min(stack))

reversed_stack = [str(x) for x in stack[::-1]]
print(", ".join(reversed_stack))
