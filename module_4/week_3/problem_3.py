import math

def read_file(file_name):
    cities = []
    with open(file_name) as file: 
        num_cities = int(file.readline().strip())
        for line in file:
            _, x, y = map(float, line.split())
            cities.append((x, y))
    return num_cities, cities

def distance(city_1, city_2):
    # Calculate distance between city_1 and city_2
    x_1, y_1 = city_1
    x_2, y_2 = city_2
    return math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

def neighbor(num_cities, cities):
    # Track visited cities 
    visited = set([0]) 
    total_cost = 0
    current_city = 0
    steps = 0
    total_steps = num_cities

    # Repeat until all cities have been visited 
    while len(visited) < num_cities:
        nearest_city = None
        nearest_distance = float('inf')

        # Find the closest city that hasn't benn visited 
        for city in range(num_cities):
            if city not in visited:
                dist = distance(cities[current_city], cities[city])
                if dist < nearest_distance:
                    nearest_city = city
                    nearest_distance = dist

        # Add that city to visited
        visited.add(nearest_city)
        total_cost += nearest_distance
        current_city = nearest_city

        # Print progress every 1000 steps
        steps += 1
        if steps % 1000 == 0:
            print(f"Progress: {steps}/{total_steps} cities visited")

    # Add the return distance to the starting city
    total_cost += distance(cities[current_city], cities[0])

    return total_cost

def main():
    num_cities, cities = read_file('nn.txt')
    cost = neighbor(num_cities, cities)
    print("Total cost:", cost)

if __name__ == "__main__":
    main()

# Output: 1203406.5012708856 (1203406)