def read_file(file_name):
    with open (file_name, "r") as file:

        # First line
        num_nodes, bit_length = map(int, file.readline().split())
        
        graph = []
        
        for line in file:
            bit = line.strip().replace(' ', '')
            graph.append(int(bit, 2))
        
    return num_nodes, bit_length, list(set(graph))

def union_find(nodes):
    # For rach node set parents and ranks 
    parents = {node: node for node in nodes}
    ranks = {node: 0 for node in nodes}
    
    return parents, ranks 

def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]

def union(parents, ranks, node_1, node_2):
    root_1 = find(parents, node_1)
    root_2 = find(parents, node_2)

    # Merge process depends on rangs 
    if root_1 != root_2:
        if ranks[root_1] > ranks[root_2]:
            parents[root_2] = root_1
        elif ranks[root_1] < ranks[root_2]:
            parents[root_1] = root_2
        else:
            parents[root_2] = root_1
            ranks[root_1] += 1


def hamming(node_1, node_2):
    return bin(node_1 ^ node_2).count('1')

def find_neighbors(node, nodes_set, bit_length):
    neighbors = []

    for i in range(bit_length):
        neighbor = node ^ (1 << i)
        if neighbor in nodes_set:
            neighbors.append(neighbor)


    for i in range(bit_length):
        for j in range(i + 1, bit_length):

            neighbor_2 = node ^ (1 << i) ^ (1 << j)

            if neighbor_2 in nodes_set:
                neighbors.append(neighbor_2)
        
    return neighbors

def process(nodes, bit_length, nodes_set):
    parents, ranks = union_find(nodes)

    for i, node in enumerate(nodes): 

        if i % 10000 == 0:
            print(f'Processing node {i+1}/ {len(nodes)}')

        # Find neighbors with 1 or 2 bits difference 
        neighbors = find_neighbors(node, nodes_set, bit_length)

        # Union current node with each of its neighbors 
        for neighbor in neighbors:
            union(parents, ranks, node, neighbor)

    # Count the number of unique clusters by finding unique representatives 
    unique_clusters = set()
    for node in nodes:

        # Find the leader of each node
        unique_clusters.add(find(parents,node))

    return len(unique_clusters)


def main():
    num_nodes, bit_length, nodes = read_file("clustering_big.txt")

    nodes_set = set(nodes)

    num_clusters = process(nodes, bit_length, nodes_set)

    print(num_clusters)


if __name__ == "__main__":
    main()

# Output: 6118