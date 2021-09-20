from io import StringIO
import sys

input1 = """10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU"""
input2 = """4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

number_of_commands = int(input())
unique_parked_cars = set()

for _ in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        unique_parked_cars.add(car_number)
    elif direction == "OUT":
        unique_parked_cars.remove(car_number)

if unique_parked_cars:
    for n in unique_parked_cars:
        print(n)
else:
    print("Parking Lot is Empty")

