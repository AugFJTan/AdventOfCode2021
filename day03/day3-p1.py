# Using the binary numbers in your diagnostic report:
# Calculate the gamma rate and epsilon rate, then multiply them together.
# What is the power consumption of the submarine?

bit_count = [0] * 12
total_samples = 0

with open('input.txt', 'r') as file:
    for line in file:
        total_samples += 1
        
        for i in range(len(line)-1):
            if line[i] == '1':
                bit_count[i] += 1

result = ''

for i in range(len(bit_count)):
    one_bits = bit_count[i]
    zero_bits = total_samples - bit_count[i]
    
    result += '1' if one_bits > zero_bits else '0'

gamma = int(result, 2)
epsilon = gamma ^ 0xfff

print(gamma * epsilon)  # Answer: 3958484
