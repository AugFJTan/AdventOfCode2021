# Determine the horizontal position to align to using the least fuel possible
# How much fuel must they spend to align to that position?

with open('input.txt', 'r') as file:
    x_positions = list(map(int, file.readline().split(',')))

result = []

for i in range(len(x_positions)):
    cost = 0
    
    for j in range(len(x_positions)):
        cost += abs(x_positions[i] - x_positions[j])
    
    result.append(cost)

print(min(result))  # Answer: 348996
