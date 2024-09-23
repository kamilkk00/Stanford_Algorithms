def read_file(file_name):
    graph = []
    with open (file_name, "r") as file:
        # Number of vertices 
        vertices = int(file.readline().strip())

        # Split nodes and cost 
        for line in file:
            node_1, node_2, cost = map(int, line.split())
            graph.append((node_1, node_2, cost))

    return vertices, graph

def union_find(nodes):
    # Create a list 
    parents = [0] * (nodes + 1)

    # For each node, set parent 
    for i in range(1, nodes + 1):
        parents[i] = i 

    return parents 
    

def find(parents, node):
    if parents[node] != node: 
        parents[node] = find(parents, parents[node])
    return parents[node]

def union(parents, node_1, node_2):
    root_1 = find(parents, node_1) 
    root_2 = find(parents, node_2) 
    if root_1 != root_2:
        parents[root_2] = root_1

def kruskal(edges, nodes, clusters):
    # Sort by cost 
    edges.sort(key=lambda edge: edge[2])

    parents = union_find(nodes)
    track = []

    for edge in edges: 
        
        # Check if vertices are in different clusters 
        if find(parents, edge[0]) != find(parents, edge[1]):
            
            # Merging edges into one cluster 
            union(parents, edge[0], edge[1])
            track.append(edge)
        
        if len(track) == nodes - clusters: 
            break

    return track, parents

def max_spacing(edges, parents): 
    for edge in edges: 
        node_1, node_2, cost = edge 
        if find(parents, node_1) != find(parents, node_2):
            return cost 
        

def main():
    vertices, graph = read_file("clustering_1.txt")

    clusters = 4 
    mst_edges, parents = kruskal(graph, vertices, clusters)
    
    max_value = max_spacing(graph, parents)

    print("Max spacing:", max_value)

if __name__ == "__main__":
    main()

# Output: 106