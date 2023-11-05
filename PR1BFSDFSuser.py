# BFS CODE
def bfs(graph, start):
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# DFS CODE
def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# Initialize an empty graph
graph = {}

# Input the graph nodes and edges interactively
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter the name of node {i + 1}: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
    graph[node] = [n.strip() for n in neighbors]

start_node = input("Enter the starting node: ")

print("Breadth-First Search (BFS):")
bfs(graph, start_node)
print("\n")

print("Depth-First Search (DFS):")
visited = set()
dfs(graph, start_node, visited)


"""Output:
Enter the number of nodes: 5
Enter the name of node 1: a
Enter neighbors of a (comma-separated): b, c
Enter the name of node 2: b
Enter neighbors of b (comma-separated): a, d
Enter the name of node 3: c
Enter neighbors of c (comma-separated): a, e
Enter the name of node 4: d
Enter neighbors of d (comma-separated): b
Enter the name of node 5: e
Enter neighbors of e (comma-separated): c
Enter the starting node: a
Breadth-First Search (BFS):
a b c d e 

Depth-First Search (DFS):
a
b
d
c
e

"""