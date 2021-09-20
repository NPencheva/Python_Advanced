from io import StringIO
import sys

input1 = """4
Ce O
Mo O Ce
Ee
Mo"""
input2 = """3
Ge Ch O Ne
Nb Mo Tc
O Ne"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

number = int(input())
unique_compounds = set()

for n in range(number):
    elements = input().split()
    for el in elements:
        if el not in unique_compounds:
            unique_compounds.add(el)

for i in unique_compounds:
    print(i)
