def kwargs_length(**kwargs):
    length = len(kwargs)

    return length


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))

dictionary_two = {}

print(kwargs_length(**dictionary_two))
