# On a seven segment display,
#  - 1 uses 2 segments
#  - 4 uses 4 segments
#  - 7 uses 3 segments
#  - 8 uses 7 segments
# In the output values, how many times do digits 1, 4, 7, or 8 appear?

count = 0

with open('input.txt', 'r') as file:
    for line in file:
        _, output_values = line.split('|')
        
        for value in output_values.split():
            if len(value) in [2, 4, 3, 7]:
                count += 1

print(count)  # Answer: 440
