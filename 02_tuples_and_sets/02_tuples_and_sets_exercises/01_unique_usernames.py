from io import StringIO
import sys

input1 = """6
George
George
George
Peter
George
NiceGuy1234"""
input2 = """10
Peter
Maria
Peter
George
Steve
Maria
Alex
Peter
Steve
George"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

number_of_usernames = int(input())
unique_usernames = set()

for _ in range(number_of_usernames):
    unique_usernames.add(input())

for username in unique_usernames:
    print(username)
