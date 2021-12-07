# Each change of 1 step in horizontal position costs 1 more unit of fuel than the last

with open('input.txt', 'r') as file:
    x_positions = list(map(int, file.readline().split(',')))

result = []

for i in range(len(x_positions)):
    cost = 0
    
    for j in range(len(x_positions)):
        n = abs(x_positions[i] - x_positions[j])
        cost += n * (n + 1) // 2  # Sum of numbers from 1 to N
    
    result.append(cost)

print(min(result))  # Answer: 98231647
