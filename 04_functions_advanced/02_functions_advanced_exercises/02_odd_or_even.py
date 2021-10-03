from io import StringIO
import sys

input1 = """Odd
1 3 5 34 7 9 12 11 13 10"""
input2 = """Even
1 3 5 7 9 13"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


def odd_or_even(command, *args):
    sum_odd = 0
    sum_even = 0
    result = 0
    if command == "Odd":
        for n in args:
            if n % 2 != 0:
                sum_odd += n
        result = sum_odd * len(args)

    if command == "Even":
        for n in args:
            if n % 2 == 0:
                sum_even += n
        result = sum_even * len(args)

    return result


print(odd_or_even(input(), *(int(el) for el in input().split())))
