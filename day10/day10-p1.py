# Find the first illegal character in each corrupted line of the navigation subsystem
# What is the total syntax error score for those errors?

from corrupted import find_illegal

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

result = 0

with open('input.txt', 'r') as file:
    for line in file:
        illegal = find_illegal(line)
        if illegal:
            result += score[illegal]

print(result)  # Answer: 268845
