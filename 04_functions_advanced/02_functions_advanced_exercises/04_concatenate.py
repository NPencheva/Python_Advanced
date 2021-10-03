def concatenate(*args):
    result_string = ""
    for el in args:
        result_string += el

    return result_string


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
