from io import StringIO
import sys

input1 = """4 6"""
input2 = """3 2"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

r, c = [int(x) for x in input().split()]
# # n = int(input())
#
#
# def read_matrix():
#     this_matrix = []
#
#     for _ in range(n):
#         row = [int(x) for x in input().split()]
#         this_matrix.append(row)
#
#     return this_matrix
#
#
# matrix = read_matrix()

for row_index in range(r):
    for col_index in range(c):
        print(f"{chr(97 + row_index)}{chr(97 + row_index + col_index)}{chr(97 + row_index)}", end=" ")
    print()



