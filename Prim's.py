# edges are 2 element tuples in format (connected_vertex, cost)
class undirected_graph:
    def __init__(self, num_vertices) -> None:
        self.vertices = [[-1 for j in range (num_vertices)] for i in range(num_vertices)]

    def add_vertex(self):
        for vertex in self.vertices:
            vertex.append(-1)
        self.vertices.append([-1 for j in range(len(self.vertices) + 1)])

    def add_edge(self, origin, destination, cost):
        self.vertices[origin][destination] = cost

def findMinimumEdgeThatConnectsVisitedToUnvisited(visited, graph):
    for i in range(len(visited)):
        if(visited[i]): # if current vertex has been visited



    return (0,0)

def prims(graph):
    mst = {""}
    mst.remove("")
    visited = [False for vertex in graph]
    current_vertex = 0
    visited[current_vertex] = True

    while len(visited) != len(graph.vertices):
        edge = findMinimumEdgeThatConnectsVisitedToUnvisited(visited, graph)
        mst.add(edge)
        visited[current_vertex] = True

#really annoying to create a graph
network = undirected_graph(5)
