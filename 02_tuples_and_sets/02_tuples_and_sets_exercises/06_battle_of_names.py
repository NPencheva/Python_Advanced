from io import StringIO
import sys

input1 = """4
Pesho
Stefan
Stamat
Gosho"""
input2 = """6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

number = int(input())
odd_set = set()
even_set = set()

for row in range(1, number + 1):
    name = input()
    result = int((sum(ord(ch) for ch in name)) / row)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(odd_set) == sum(even_set):
    final = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    final = odd_set.difference(even_set)
else:
    final = odd_set.symmetric_difference(even_set)

print(", ".join(str(el) for el in final))
