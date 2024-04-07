# 漢密爾頓迴圈 (Hamiltonian Cycle)
# 演算法分析機測
# 學號: 11020117 / 11020126 / 11020134
# 姓名: 林子皓 / 鄭祐昀 / 呂宗凱
# 中原大學電機資訊學士班
def is_valid(v, pos, path, graph):
    # Check if this vertex is an adjacent vertex of the previously added vertex.
    if graph[path[pos-1]][v] == 0:
        return False
    # Check if the vertex has already been included.
    for vertex in path:
        if vertex == v:
            return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    # base case: if all vertices are included in the path
    if pos == len(graph):
        # And if there is an edge from the last included vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as a next candidate in Hamiltonian Cycle.
    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            # Remove current vertex if it doesn't lead to a solution
            path[pos] = -1

    return False

def find_hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Start at the first vertex

    if not hamiltonian_cycle_util(graph, path, 1):
        return None
    else:
        # Return the path plus one to convert from 0-based to 1-based index
        return [vertex + 1 for vertex in path]

# Now we need to build the graph based on the input provided. For this, we will first parse the input
# to extract the vertices and edges, and then create the adjacency matrix for the graph.

# input the graph information
num_vertices, num_edges = map(int, input().split())

# Initialize the edges list
edges = []

# input the edges until "0 0" is entered
while True:
    edge = tuple(map(int, input().split()))
    if edge == (0, 0):
        break
    edges.append(edge)

# Create the graph as an adjacency matrix
graph = [[0] * num_vertices for _ in range(num_vertices)]
for edge in edges:
    v1, v2 = edge
    graph[v1-1][v2-1] = 1
    graph[v2-1][v1-1] = 1  


hamiltonian_cycle = find_hamiltonian_cycle(graph)
# Add the first vertex to the end to complete the cycle
hamiltonian_cycle.append(hamiltonian_cycle[0])
hamiltonian_cycle

# Create the graph as an adjacency matrix
graph = [[0] * num_vertices for _ in range(num_vertices)]
for edge in edges:
    v1, v2 = edge
    graph[v1-1][v2-1] = 1
    graph[v2-1][v1-1] = 1  # Since the graph is undirected

# Let's find a Hamiltonian cycle.
hamiltonian_cycle = find_hamiltonian_cycle(graph)
# Add the first vertex to the end to complete the cycle
hamiltonian_cycle.append(hamiltonian_cycle[0])
hamiltonian_cycle

print(hamiltonian_cycle)
