from io import StringIO
import sys

input1 = """8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey"""
input2 = """7
Lyle
Bruce
Alice
Easton
Shawn
Alice
Shawn"""
input3 = """6
Adam
Adam
Adam
Adam
Adam
Adam"""
# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

number = int(input())
unique_names = {input() for n in range(number)}

for name in unique_names:
    print(name)
