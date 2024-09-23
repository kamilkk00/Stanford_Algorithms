from collections import defaultdict


def main():
    graph = load_file()
    reversed_graph = reverse_graph(graph)
    
    # First DFS on reversed graph
    ordered_vertices = first_dfs_new_graph(reversed_graph)

    # Second DFS on original graph, using order from first pass
    sccs = second_dfs_old_graph(graph, reversed(ordered_vertices))

    top_5_scc = scc_sort(sccs)

    print (top_5_scc)

def load_file():
    num_verticies = 875714
    graph = defaultdict(list)

    # Opening the file 
    with open ("scc.txt", "r") as file:
        for line in file:

            # Splitting file into vertex start: u and ending: v
            u, v = map(int, line.split())

            # Adding v to list of vertex u 
            graph[u].append(v)

    # Checking if all verticies exist in the graph 
    for i in range(1, num_verticies + 1):
        if i not in graph:
            graph[i]=[]

    return graph 

def reverse_graph(graph):
    num_verticies = 875714
    new_graph = defaultdict(list)

    for u in graph:
        for v in graph[u]:

            # Adding u to list
            new_graph[v].append(u)

    # Checking if all vertices are in new_graph
    for i in range(1, num_verticies + 1):
        if i not in new_graph:
            new_graph[i] = []

    return new_graph

def dfs_new(graph, start_vertex, visited, list_visited):
    stack = [(start_vertex, False)]

    # Loop while stack is not empty 
    while stack:

        # Pop the last element 
        v, is_returning = stack.pop() 

        # Check if v has been visited 
        if v not in visited:

            # Mark as visited 
            visited.add(v)

            # Add to the stack 
            stack.append((v, True))
            
            # Checking all neighbors 
            for neighbor in graph[v]:
            
                # If neighbor hasn't been visited, add them 
                if neighbor not in visited:
                    stack.append((neighbor, False))
        elif is_returning:
            list_visited.append(v)


def first_dfs_new_graph(graph):

    # Empty set to track visited verticies 
    visited = set()

    # Storing verticies in order of finished time 
    list_visited = []

    # Loop through all verticies in graph 
    for v in graph:

        # If vertex hasn't been visited 
        if v not in visited:
            dfs_new(graph, v, visited, list_visited)

    return list_visited

def dfs_old(graph, start_vertex, visited, current_scc):
    
    # Starting with start vertex 
    stack = [start_vertex]
    
    # While stack is not empty 
    while stack:

        # Download last element from stack 
        v = stack.pop()

        # Check if vertex has been visited 
        if v not in visited:

            # If not add
            visited.add(v)
            current_scc.append(v)

            # Check and add neighbor if they hasn't been added
            for neighbor in graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)



def second_dfs_old_graph(graph, ordered_vertices):
    
    # Set to track visited vertices 
    visited = set()

    # Store all SCC
    scc_list = []

    # Check all vertices in reverse finishing order 
    for v in ordered_vertices:

        # If vertax hasn't been visited 
        if v not in visited:

            # New list for the current SCC
            current_scc = []

            # DFS starting from vertex v to find all verticies 
            dfs_old(graph, v, visited, current_scc)

            # Append SCC to the list 
            scc_list.append(current_scc)

    return scc_list

def scc_sort(scc_list):
    scc_sizes = []

    # Calculate sizes and pair them with SCCs
    for scc in scc_list:
        length = len(scc)
        scc_sizes.append((length, scc))

    # Sort by size 
    scc_sizes.sort(reverse=True, key=lambda x: x[0])

    top_5_scc = [size for size, _ in scc_sizes[:5]]

    while len(top_5_scc) < 5:
        top_5_scc.append(0)

    return top_5_scc


if __name__ == "__main__":
    main()

# Output: 434821, 968, 459, 313, 211
