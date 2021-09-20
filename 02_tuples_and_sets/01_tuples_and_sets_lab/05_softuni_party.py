from io import StringIO
import sys

input1 = """5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END"""
input2 = """6
m8rfQBvl
fc1oZCE0
UgffRkOn
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

number_of_guests = int(input())
invited_guests = set()
attending_guests = set()

for _ in range(number_of_guests):
    invited_guests.add(input())

while True:
    command = input()
    if command == "END":
        break
    else:
        attending_guests.add(command)

not_attending_guests = sorted(invited_guests.difference(attending_guests))

print(len(not_attending_guests))

for guest in not_attending_guests:
    print(guest)
