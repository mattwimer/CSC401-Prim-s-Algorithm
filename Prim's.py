class undirected_graph:
    def __init__(self, num_vertices) -> None:
        self.vertices = [[-1 for j in range (num_vertices)] for i in range(num_vertices)]

    def add_vertex(self):
        for vertex in self.vertices:
            vertex.append(-1)
        self.vertices.append([-1 for j in range(len(self.vertices) + 1)])

    def add_edge(self, v1, v2, cost):
        self.vertices[v1][v2] = cost
        self.vertices[v2][v1] = cost

def findMinimumEdgeThatConnectsVisitedToUnvisited(visited, graph):
    for i in range(len(visited)):
        if not visited[i]:
            minCost = -1
            bestEdge = -1
            for j in range(len(graph[i])):
                if visited[j] and (graph[i][j] < minCost or (graph[i][j] != -1 and minCost == -1)):
                    minCost = graph[i][j]
                    bestEdge = j
            return (i, bestEdge)
                    
    return (0,0) # finished

def prims(graph):
    mst = {""}
    mst.remove("")
    visited = [False for vertex in graph.vertices]
    # current_vertex = 0
    visited[0] = True

    while [1 for vertex in visited if not vertex]: # if any vertices havent been visited, list is non empty and loop will run
        edge = findMinimumEdgeThatConnectsVisitedToUnvisited(visited, graph.vertices)
        if edge[1] != -1:
            mst.add(str(edge))
        visited[edge[0]] = True
        # current_vertex+=1

    return mst

#really annoying to create a graph
network1 = undirected_graph(4)

# (origin, destination, cost)
for edge in [(0,1,3), (0,2,1), (1,2,2), (2,3,4)]:
    network1.add_edge(*edge)

print(prims(network1))

network2 = undirected_graph(4)

# (origin, destination, cost)
#                     vvv same cost vvv
for edge in [(0,1,3), (0,2,2), (1,2,2), (2,3,4)]:
    #                 ^^^ same cost ^^^
    network2.add_edge(*edge)

print(prims(network2))

network3 = undirected_graph(4)

# (origin, destination, cost)
# no connection to 4th vertex
for edge in [(0,1,3), (0,2,1), (1,2,2)]:
    network3.add_edge(*edge)

print(prims(network3))