file = open("numbers.txt", "r")

sum_lines = 0

for line in file:
    sum_lines += int(line)

print(sum_lines)
