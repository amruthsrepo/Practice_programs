class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices
        self.graph = graph

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited
    
def get_shortest_time(startNode, endNode, paths):
    vertices = set()
    edges = {}
    for s,e,c in paths:
        vertices.add(s)
        vertices.add(e)
        edges[s] = edges.get(s, {})
        edges[s][e] = int(c)
        # edges.append((s,e,int(c)))
    g = Dijkstra(vertices, edges)
    print(g.find_route(startNode, endNode)[1].get(e,-1))
    
get_shortest_time('S0', 'S4', [
    ('S0', 'S11', '16'),
    ('S0', 'S12', '22'),
    ('S0', 'S13', '18'),
    ('S11', 'S21', '8'),
    ('S12', 'S21', '12'),
    ('S12', 'S22', '13'),
    ('S13', 'S21', '15'),
    ('S13', 'S22', '11'),
    ('S21', 'S31', '7'),
    ('S21', 'S32', '21'),
    ('S22', 'S31', '17'),
    ('S22', 'S32', '13'),
    ('S22', 'S33', '19'),
    ('S31', 'S4', '9'),
    ('S32', 'S4', '18'),
    ('S33', 'S4', '20'),
])