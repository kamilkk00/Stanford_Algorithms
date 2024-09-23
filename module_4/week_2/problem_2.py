import math

def read_file(file_name):
    cities = []
    with open(file_name) as file: 
        num_cities = int (file.readline().strip())
        for line in file:
            city = list(map(float, line.split()))
            cities.append(city)

    return num_cities, cities 
        
def distances(num_cities, cities):
    distance = [[0] * num_cities for _ in range(num_cities)]

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            
            # Coordinates of city i, j
            x_1, y_1 = cities[i]
            x_2, y_2 = cities[j]

            # Calculate distance between city i, j
            dist = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

            # Update distance into matrix 
            distance[i][j] = dist
            distance[j][i] = dist

    return distance


def held_karp(num_cities, matrix):
    dp = [[math.inf] * num_cities for _ in range(1 << num_cities)]
    dp[1][0] = 0

    total_steps = (1 << num_cities) * num_cities
    step = 0


    for bits in range(1 << num_cities):
        for city in range(1, num_cities):

            step += 1
            if step % 1000 == 0:
                print(f"Progress: {step}/{total_steps} steps completed")

            if bits & (1 << city):
                prev_bits = bits & ~(1 << city)
                for prev_city in range(num_cities):
                    if prev_bits & (1 << prev_city):
                        dp[bits][city] = min(dp[bits][city], dp[prev_bits][prev_city] + matrix[prev_city][city])

    all_visited = (1 << num_cities) - 1
    result = min(dp[all_visited][city] + matrix[city][0] for city in range(1, num_cities))

    return result

def main():
    num_cities, cities = read_file('tsp.txt')
    
    matrix = distances(num_cities, cities)

    result = held_karp(num_cities, matrix)

    print(result)



if __name__ == "__main__":
    main()

# Output: 26442.73030895475 (26442)