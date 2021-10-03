def operate(operator, *args):
    result = args[0]
    for n in args[1:]:
        if operator == "+":
            result += n
        elif operator == "-":
            result -= n
        elif operator == "*":
            result *= n
        elif operator == "/":
            result /= n

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 4, 0))