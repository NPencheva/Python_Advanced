def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    list_odd = []
    list_even = []
    if command == "odd":
        for n in numbers:
            if n % 2 != 0:
                list_odd.append(n)
        return list_odd
    elif command == "even":
        for n in numbers:
            if n % 2 == 0:
                list_even.append(n)
        return list_even


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
