# permutations

def permutations(index, values):
    if index == len(values):
        print("".join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permutations(index + 1, values)
        values[i], values[index] = values[index], values[i]


permutations(0, list(input()))

