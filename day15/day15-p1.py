# Find the lowest total risk of any path from the top left to the bottom right

from pathfinding import *


# Apply A* search algorithm
env = Environment()

astar = AStar(env)
astar.search()


# Get risk from path
path = astar.path
path.pop()

total_risk = 0

for node in path:
    total_risk += node.risk

print(total_risk)  # Answer: 415
