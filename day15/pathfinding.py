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
        
        self.generate_graph()
        
        self.graph_width = len(self.graph[0])
        self.graph_height = len(self.graph)

        self.start = self.graph[0][0]
        self.goal = self.graph[self.graph_height-1][self.graph_width-1]


    def generate_graph(self):
        with open('input.txt', 'r') as file:
            for y, line in enumerate(file):
                risk = list(map(int, line.rstrip()))
                nodes = []
                
                for x, r in enumerate(risk):
                    nodes.append(Node(x, y, r))
                
                self.graph.append(nodes)


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


class FullEnvironment(Environment):
    def __init__(self):
        super().__init__()


    def generate_graph(self):
        base_tile = []
        
        with open('input.txt', 'r') as file:
            for line in file:
                risk = list(map(int, line.rstrip()))
                base_tile.append(risk)
        
        base_width = len(base_tile[0])
        base_height = len(base_tile)
        
        for _ in range(base_height * 5):
            self.graph.append([None] * (base_width * 5))
        
        # Calculate risk horizontally
        for y in range(base_height):
            for x in range(base_width):
                risk = base_tile[y][x]
                
                for i in range(5):
                    if risk > 9:
                        risk = 1
                    
                    dx = i * base_width
                    self.graph[y][x + dx] = Node(x + dx, y, risk)
                    
                    risk += 1
        
        # Calculate risk vertically
        for y in range(base_height):
            for x in range(base_width * 5):
                risk = self.graph[y][x].risk + 1
                
                for i in range(1, 5):
                    if risk > 9:
                        risk = 1
                        
                    dy = i * base_height
                    self.graph[y + dy][x] = Node(x, y + dy, risk)
                    
                    risk += 1


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
