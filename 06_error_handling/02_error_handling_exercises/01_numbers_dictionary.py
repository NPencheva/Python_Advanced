numbers_dictionary = {}

line = input()

value_error_message = "The variable number must be an integer"
key_error_message = "Number does not exist in dictionary"

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(value_error_message)
    line = input()

line = input()

while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print(key_error_message)
    line = input()

line = input()

while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print(key_error_message)
    line = input()

print(numbers_dictionary)
