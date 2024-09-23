import heapq


def file(file_name):
    with open(file_name, "r") as file:
        nodes, edges = list(map(int, file.readline().split()))

        adj_list = {i: [] for i in range(1, nodes + 1)}

        for line in file: 
            node_1, node_2, cost = map(int, line.split())

            adj_list[node_1].append((node_2, cost))
            adj_list[node_2].append((node_1, cost))
        
    return adj_list

def prim(graph):

    visited = set()
    
    start_node = 1
    
    visited.add(start_node)

    edges = []

    # Adding edges to the heap
    for neighbor, cost in graph[start_node]:
        heapq.heappush(edges, (cost, start_node, neighbor))

    total_cost = 0 

    # For unvisited nodes 
    while edges: 
        # Get the edge with minimum cost from the heap 
        cost, node_1, node_2 = heapq.heappop(edges)

        # If target hasn't been visited 
        if node_2 not in visited: 
            visited.add(node_2)
            total_cost += cost 

            # Add all egdes from the newly visited node to the heap 
            for neighbor, edge_cost in graph[node_2]:
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_cost, node_2, neighbor))
    
    return total_cost

def main():
    read_file = file("edges.txt")
    total_cost = prim(read_file)
    print("Total cost", total_cost)

if __name__ == "__main__":
    main()

# Output: -3612829