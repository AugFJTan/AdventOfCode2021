# A basin is all locations that eventually flow downward to a single low point
# Locations of height 9 do not count as being in any basin
# Find the three largest basins and multiply their sizes together

with open('input.txt', 'r') as file:
    heightmap = []
    
    for line in file:
        heightmap.append(list(map(int, list(line.rstrip()))))

map_width = len(heightmap[0])
map_height = len(heightmap)


def flood_fill(search, pos):
    if heightmap[pos[0]][pos[1]] == 9:
        return
    
    if pos in search:
        return
    
    search.append(pos)
    
    # Top
    if pos[0] > 0:
        flood_fill(search, (pos[0]-1, pos[1]))
    
    # Bottom
    if pos[0] < map_height-1:
        flood_fill(search, (pos[0]+1, pos[1]))
    
    # Left
    if pos[1] > 0:
        flood_fill(search, (pos[0], pos[1]-1))
    
    # Right
    if pos[1] < map_width-1:
        flood_fill(search, (pos[0], pos[1]+1))


basins = []

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
            search = []
            flood_fill(search, (i, j))
            basins.append(len(search))


results = sorted(basins)

print(results[-1] * results[-2] * results[-3])  # Answer: 1269555
