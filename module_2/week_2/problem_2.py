import heapq

def read_file():
    graph = {}

    # Read each line of file 
    with open('data.txt', "r") as file:

        # Split lines into vertex and rest
        for line in file: 
            parts = line.split()
            vertex = int(parts[0])
            
            # Ensure that vertex is in graph 
            if vertex not in graph:
                graph[vertex] = []

            # Iterate over the neighbor / weight pairs
            for pair in parts[1:]:
                neighbor, weight = map(int, pair.split(','))
                
                # Adding edge from vertex to neighbor 
                graph[vertex].append((neighbor, weight))

                # Adding the reverse edge (undirected graph)
                if neighbor not in graph:
                    graph[neighbor] = []
                graph[neighbor].append((vertex, weight))

        return graph


def dijkstra(graph, start_vertex):
    distances = {}

    # Initial distance for each vertex (large number)
    for vertex in graph:
        distances[vertex] = 10000000

    # Distance for start vertex as 0 
    distances[start_vertex] = 0 

    queue = []

    # Adding start vertex to the priority queue (distance of 0)
    heapq.heappush(queue, (0, start_vertex))

    while queue:

        # Extract vertex with smallest distance from queue
        current_distance, current_vertex = heapq.heappop(queue)

        # If current distance is grater than the stored distance, skip 
        if current_distance > distances[current_vertex]:
            continue

        # For each neighbor of the current vertex 
        for neighbor, weight in graph[current_vertex]:

            # Calculate distance 
            distance = current_distance + weight

            # If the new distance is shorter, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance 

                # Add neighbor to queue with updated distance 
                heapq.heappush(queue, (distance, neighbor))
        
    return distances

def vertex_distance(distances, vertices):

    results = []

    for vertex in vertices:
        # Checking if distance to vertex is less than large number 
        if distances[vertex] < 10000000:
            results.append(distances[vertex])
        else:
            results.append(1000000)

    return results


def main():

    # Read graph 
    graph = read_file()

    # Set start vertex 
    start_vertex = 1 

    distances = dijkstra(graph, start_vertex)

    # List of vertices for which to get distances 
    vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

    # Getting the result from the vertex_distance function 
    results = vertex_distance(distances, vertices)

    print(results)

if __name__ == "__main__":
    main()

# Output: 2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068