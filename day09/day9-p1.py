# The risk level of a low point is 1 plus its height.
# What is the sum of the risk levels of all low points on your heightmap?

with open('input.txt', 'r') as file:
    heightmap = []
    
    for line in file:
        heightmap.append(list(map(int, list(line.rstrip()))))

map_width = len(heightmap[0])
map_height = len(heightmap)

risk_level = 0

for i in range(map_height):
    for j in range(map_width):
        current = heightmap[i][j]
        adjacent = []
        
        # Top
        if i > 0:
            adjacent.append(heightmap[i-1][j])
        
        # Bottom
        if i < map_height-1:
            adjacent.append(heightmap[i+1][j])

        # Left
        if j > 0:
            adjacent.append(heightmap[i][j-1])
        
        # Right
        if j < map_width-1:
            adjacent.append(heightmap[i][j+1])
        
        lowest = True
        
        for area in adjacent:
            if current >= area:
                lowest = False
        
        if lowest:
            risk_level += current + 1

print(risk_level)  # Answer: 465
