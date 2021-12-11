# Given the starting energy levels of the dumbo octopuses simulate 100 steps
# How many total flashes are there after 100 steps?

import octo_flash as ocfl

steps = 100
octo_map = []

with open('input.txt', 'r') as file:
    for line in file:
        octo_map.append(list(map(int, list(line.rstrip()))))

for _ in range(steps):
    # Increment energy of each octopus by 1
    for i in range(10):
        for j in range(10):
            octo_map[i][j] += 1
    
    # Compute chain flashes
    for i in range(10):
        for j in range(10):
            if octo_map[i][j] >= 10:
                ocfl.flash(octo_map, (i, j))

print(ocfl.flash_count)  # Answer: 1741
