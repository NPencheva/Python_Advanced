# https://judge.softuni.org/Contests/3159

from io import StringIO
import sys

input1 = """1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset"""
input2 = """5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

first_seq = set(int(el) for el in input().split())
second_seq = set(int(el) for el in input().split())
number = int(input())

for _ in range(number):
    command_line = input().split()
    command = " ".join(command_line[:2])
    numbers_seq = set([int(el) for el in command_line[2:]])

    if command == "Add First":
        first_seq = first_seq.union(numbers_seq)
    elif command == "Add Second":
        second_seq = second_seq.union(numbers_seq)
    elif command == "Remove First":
        first_seq = first_seq.difference(numbers_seq)
    elif command == "Remove Second":
        second_seq = second_seq.difference(numbers_seq)
    elif command == "Check Subset":
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(", ".join(str(el) for el in sorted(first_seq)))
print(", ".join(str(el) for el in sorted(second_seq)))
