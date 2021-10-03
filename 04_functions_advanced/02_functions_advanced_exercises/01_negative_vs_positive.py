# https://judge.softuni.org/Contests/1839
#
from io import StringIO
import sys

input1 = """1 2 -3 -4 65 -98 12 57 -84"""
input2 = """1 2 3"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)


def negative_vs_positive(*args):
    sum_negative = 0
    sum_positive = 0
    for n in args:
        if n > 0:
            sum_positive += n
        else:
            sum_negative += n

    print(sum_negative)
    print(sum_positive)
    if abs(sum_positive) > abs(sum_negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = (int(el) for el in input().split())

negative_vs_positive(*numbers)
