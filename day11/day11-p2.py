# What is the first step during which all octopuses flash?

import octo_flash as ocfl

octo_map = []

with open('input.txt', 'r') as file:
    for line in file:
        octo_map.append(list(map(int, list(line.rstrip()))))

step_count = 0

while True:
    step_count += 1

    # Increment energy of each octopus by 1
    for i in range(10):
        for j in range(10):
            octo_map[i][j] += 1
    
    # Compute chain flashes
    for i in range(10):
        for j in range(10):
            if octo_map[i][j] >= 10:
                ocfl.flash(octo_map, (i, j))
    
    # Check if all octopuses flash simultaneously
    all_flash = True
    
    for i in range(10):
        for j in range(10):
            if octo_map[i][j] != 0:
                all_flash = False
    
    if all_flash:
        break

print(step_count)  # Answer: 440
