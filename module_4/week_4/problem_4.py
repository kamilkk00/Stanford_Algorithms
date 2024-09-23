from collections import defaultdict

def read_file(file_name):
    clauses = []
    with open(file_name, 'r') as file:
        num_variables = int (file.readline().strip())

        for line in file: 
            claus = tuple(map(int, line.split()))
            clauses.append(claus)

    return num_variables, clauses

def graph(num_variables, clauses):
    graph = defaultdict(list)

    def var_to_index(var):
        # x1 -> x2 
        if var > 0:
            return 2 * (var - 1)
        # -x2 -> -x1   
        else: 
            return 2 * (-var - 1) + 1 

    # Build graph from clauses 
    for x, y in clauses:
        graph[var_to_index(-x)].append(var_to_index(y))
        graph[var_to_index(-y)].append(var_to_index(x))

    return graph 

def kosaraju(num_variables, graph, reverse_graph):

    # Perform DFS on the reverse graph to detemine the finish order 
    visited = set()
    finish_stack = []

    # Perform DFS on the reversed graph 
    for node in range(2 * num_variables):
        if node not in visited:
            dfs(reverse_graph, node, visited, finish_stack)

    # Perform DFS on the original graph using the nodes in reverse finishing order 
    visited.clear()
    sccs=[]

    # Process nodes in decreasing finishing time order 
    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            scc = []
            dfs(graph, node, visited, scc)
            sccs.append(scc)

    # Check if any SCC contains both a variable and its negation
    assignment = [None] * num_variables
    for scc in sccs: 
        for node in scc:
            var = node // 2
            is_negated = node % 2 == 1

            # If both the variable and its negation are in the same SCC, the formula is unsatisfiable 
            if (is_negated and (2 * var ) in scc) or (not is_negated and (2 * var + 1) in scc):
                return False 
        
        # If haven't seen this variable before, assign a value 
        if assignment[var] is None:
            assignment[var] = not is_negated 

    return True

def dfs(graph, node, visited, stack=None):

    visited.add(node)

    # Visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    
    if stack is not None:
        stack.append(node)


def check(sccs):
    pass

def main():
    #num_variables, clauses = read_file("2_sat_1.txt")
    #num_variables, clauses = read_file("2_sat_2.txt")
    #num_variables, clauses = read_file("2_sat_3.txt")
    #num_variables, clauses = read_file("2_sat_4.txt")
    #num_variables, clauses = read_file("2_sat_5.txt")
    num_variables, clauses = read_file("2_sat_6.txt")

    original_graph = graph(num_variables, clauses)

    # Buil reverse_graph
    reverse_graph = defaultdict(list)
    for node in original_graph:
        for neighbor in original_graph[node]:
            reverse_graph[neighbor].append(node)
    
    result = kosaraju(num_variables, original_graph, reverse_graph)

    if result:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()

"""
Output:
- sat_1: 1 
- sat_2: 0
- sat_3: 1
- sat_4: 1
- sat_5: 0
- sat_6: 0
"""