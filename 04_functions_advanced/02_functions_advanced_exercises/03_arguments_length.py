# from io import StringIO
# import sys
#
# input1 = """Odd
# 1 3 5 34 7 9 12 11 13 10"""
# input2 = """Even
# 1 3 5 7 9 13"""
#
# sys.stdin = StringIO(input1)
# # sys.stdin = StringIO(input2)


def args_length(*args):
    length = len(args)

    return length


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
