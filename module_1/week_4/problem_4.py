import random
import copy

with open("karger.txt", "r") as file:
    graph = {}
    for line in file: 
        # Spliting lines into numbers 
        parts = list(map(int, line.split()))
        # First number (vertex) 
        vertex = parts[0]
        # Vertex's neighbors 
        neighbors = parts[1:]
        # Storing vertex and neighbours  
        graph[vertex] = neighbors

def main():
    result = find_min_cut()
    print("Minimum cuting graph:", result)

def choosing_edge(graf):
    # Choosing random vertex
    random_vertex = random.choice(list(graf.keys()))

    # Choosing random neighbor of vertex
    random_neighbor = random.choice(graf[random_vertex])

    return (random_vertex, random_neighbor)

def shrink_edge(graph, random_vertex, random_neighbor):
    # Merging random_vertex with random_neighbor
    graph[random_vertex].extend(graph[random_neighbor])

    # Checking each vertex in the graph that has a connection with random_neighbor 
    for vertex in graph: 
        graph[vertex] = [random_vertex 
                        if neighbor == random_neighbor 
                        else neighbor 
                        for neighbor in graph[vertex]]
        
    # Removing self-loops from neighbors 
    graph[random_vertex] = [neighbor for neighbor in graph[random_vertex]
                            if neighbor != random_vertex]
    
    # Deleting random_neigbor from the graph
    del graph [random_neighbor]

def karger_min_cut():
    graph_copy = copy.deepcopy(graph)

    # Loop until two vertices remain 
    while len(graph_copy) > 2:
        random_vertex = random.choice(list(graph_copy.keys()))
        random_neighbor = random.choice(graph_copy[random_vertex])

        # Contracting the vertices 
        shrink_edge (graph_copy, random_vertex, random_neighbor)

    # Counting edges (2 verticies) 
    remaining_vertices = list(graph_copy.keys())
    min_cut = len(graph_copy[remaining_vertices[0]])

    return min_cut

def find_min_cut():

    # Infinity as default value 
    min_cut = float('inf')

    # Repetition times 
    x = 30

    # Checking if program found least cut in new try 
    for i in range(x):
        result = karger_min_cut()
        
        # Updating minimum cuts
        if result < min_cut:
            min_cut = result 

    return min_cut

if __name__ == "__main__":
    main()

# Output: 17