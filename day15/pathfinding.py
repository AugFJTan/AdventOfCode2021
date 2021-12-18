from enum import Enum, auto

class NodeState(Enum):
    UNDISCOVERED = auto()
    DISCOVERED = auto()
    EXPLORED = auto()


class Node:
    def __init__(self, x, y, risk):
        self.x = x
        self.y = y
        self.risk = risk
        self.state = NodeState.UNDISCOVERED
        self.parent = None


class Environment:
    def __init__(self):
        self.graph = []

        with open('input.txt', 'r') as file:
            for y, line in enumerate(file):
                risk = list(map(int, line.rstrip()))
                nodes = []
                
                for x, r in enumerate(risk):
                    nodes.append(Node(x, y, r))
                
                self.graph.append(nodes)
        
        self.graph_width = len(self.graph[0])
        self.graph_height = len(self.graph)

        self.start = self.graph[0][0]
        self.goal = self.graph[self.graph_height-1][self.graph_width-1]


    def get_adjacent(self, node):
        adjacent = []
        x, y = node.x, node.y
        
        # Right
        if x < self.graph_width-1:
            adjacent.append(self.graph[y][x+1])

        # Down
        if y < self.graph_height-1:
            adjacent.append(self.graph[y+1][x])
        
        # Left
        if x > 0:
            adjacent.append(self.graph[y][x-1])
        
        # Up
        if y > 0:
            adjacent.append(self.graph[y-1][x])
        
        return adjacent


class AStar:
    def __init__(self, env):
        self.env = env
        self.path = []


    def search(self):
        gScore = {}
        fScore = {}

        start = self.env.start
        goal = self.env.goal

        self.path = []

        openSet = [start]
        gScore[start] = 0
        fScore[start] = hScore(start, goal)

        while openSet:
            current = openSet.pop()
            current.state = NodeState.EXPLORED
            
            if current == goal:
                self.path.append(current)
            
                while current.parent:
                    current = current.parent
                    self.path.append(current)
                
                break

            adjacent_nodes = self.env.get_adjacent(current)

            for adj in adjacent_nodes:
                tentative_g = gScore[current] + adj.risk
                
                if adj.state == NodeState.UNDISCOVERED:
                    gScore[adj] = 10000  # Infinity
                    adj.state = NodeState.DISCOVERED

                if tentative_g < gScore[adj]:
                    adj.parent = current
                    gScore[adj] = tentative_g;
                    fScore[adj] = gScore[adj] + hScore(adj, goal)

                    if adj not in openSet:
                        openSet.append(adj)
            
            openSet.sort(key=lambda n: fScore[n], reverse=True) 


def hScore(start, end):
    dx = abs(start.x - end.x)
    dy = abs(start.y - end.y)
    return dx + dy
