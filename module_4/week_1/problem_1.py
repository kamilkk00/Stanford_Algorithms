def read_file(file_name):
    graph = []
    with open (file_name, "r")as file: 
        num_vertices, num_edges = map(int, file.readline().split())
        for line in file:
            vertex_start, vertex_end, distance = map(int, line.split())
            graph.append((vertex_start, vertex_end, distance))

    return num_vertices, num_edges, graph

def distance(num_vertices, edges):
    
    # Matrix to represent the distance between vertices 
    matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Set the istance for each vertex
    for i in range(num_vertices):
        matrix[i][i] = 0

    # Update the matrix with edges and distances 
    for start_vertex, end_vertex, distance in edges:
        matrix[start_vertex - 1][end_vertex - 1] = distance

    return matrix

def floyd_warshall(num_vertices, matrix):
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):

                # New potential shorter distance 
                new_distance = matrix[i][k] + matrix[k][j]

                # If distance is shorten, update the matrix 
                if new_distance < matrix[i][j]:
                    matrix[i][j] = new_distance

    return matrix 

def negative_cycle(num_vertices, matrix):

    # Checking if any element is negative 
    for i in range(num_vertices):
        if matrix[i][i] < 0: 
            return True
    
    return False 
    

def shortest_path(num_vertices, matrix):
    shortest = float('inf')

    # If the current path is shorter then the current shortest, update value 
    for i in range(num_vertices):
        for j in range(num_vertices):
            if matrix[i][j] < shortest:
                shortest = matrix[i][j] 

    return shortest 

def main():
    #num_vertices, num_edges, graph = read_file('g1.txt')
    #num_vertices, num_edges, graph = read_file('g2.txt')
    num_vertices, num_edges, graph = read_file('g3.txt')

    matrix = distance(num_vertices, graph)

    updated_matrix = floyd_warshall(num_vertices, matrix)

    result_negative_cycle= negative_cycle(num_vertices, updated_matrix)

    if result_negative_cycle == True:
        print("Null")
    else: 
        result_shortest_path = shortest_path(num_vertices, updated_matrix)
        print("Shortest path:", result_shortest_path) 

if __name__ == "__main__":
    main()

"""
Output: 
- g1: Null
- g2: Null
- g3: -19
"""