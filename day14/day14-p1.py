# Apply 10 steps of pair insertion to the polymer template
# Find difference between quantity of the most common element and least common element

with open('input.txt', 'r') as file:
    template = file.readline().rstrip()

    file.readline()  # Skip blank line
    
    rules = {}
    
    for line in file:
        pair, insert = line.rstrip().split(' -> ')
        rules[pair] = insert


for _ in range(10):
    result = ''

    for i in range(len(template)-1):
        pair = template[i:i+2]
        result += pair[0] + rules[pair]

    result += pair[1]
    
    template = result


most_common = max(result, key=result.count)
least_common = min(result, key=result.count)

print(result.count(most_common) - result.count(least_common))  # Answer: 3831
