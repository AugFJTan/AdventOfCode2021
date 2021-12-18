# Find the lowest total risk of any path from the top left to the bottom right

cave_graph = []

with open('sample.txt', 'r') as file:
    for line in file:
        risk = list(map(int, line.rstrip()))
        nodes = []
        
        for r in risk:
            # cost, risk, visited, parent
            nodes.append([100000, r, False, None])
        
        cave_graph.append(nodes)


cave_width = len(cave_graph[0])
cave_height = len(cave_graph)


def get_adjacent(pos, graph):
    adjacent = []
    x, y = pos
    
    # Right
    if x < cave_width-1:
        if graph[y][x+1][2] == False:
            adjacent.append((x+1, y))

    # Down
    if y < cave_height-1:
        if graph[y+1][x][2] == False:
            adjacent.append((x, y+1))
    
    # Left
    if x > 0:
        if graph[y][x-1][2] == False:
            adjacent.append((x-1, y))
    
    # Up
    if y > 0:
        if graph[y-1][x][2] == False:
            adjacent.append((x, y-1))
    
    return adjacent


cave_graph[0][0][0] = 0  # Set cost of first node to 0

current_pos = (0, 0)
dest_pos = (cave_width-1, cave_height-1)

search = [current_pos]
path = []


while search:
    current_pos = search.pop(0)
    cx, cy = current_pos
    
    cave_graph[cy][cx][2] = True  # Mark current node as visited
    
    # Found destination
    if current_pos == dest_pos:
        parent = cave_graph[cy][cx][3]
        
        path.append(current_pos)
        
        while parent:
            px, py = parent
            path.append(parent)
            parent = cave_graph[py][px][3]
        
        break

    adj = get_adjacent(current_pos, cave_graph)

    for a in adj:
        ax, ay = a
        
        # cost = cost so far + risk
        current_cost = cave_graph[cy][cx][0] + cave_graph[cy][cx][1]
        adjacent_cost = cave_graph[ay][ax][0] + cave_graph[ay][ax][1]
        
        if current_cost < adjacent_cost:
            # new cost = cost so far + new risk + 1 movement distance
            cost_so_far = cave_graph[cy][cx][0] + cave_graph[ay][ax][1] + 1
            
            cave_graph[ay][ax][0] = cost_so_far  # Cost
            cave_graph[ay][ax][3] = (cx, cy)     # Parent
            
            search.append((ax, ay))


path.pop(-1)  # Remove start node
total_risk = 0

for node in path:
    x, y = node
    total_risk += cave_graph[y][x][1]

print(total_risk)  # not 440 (too high)
