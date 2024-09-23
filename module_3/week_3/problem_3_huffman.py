import heapq

def read_file(file_name):
    weights = []
    with open(file_name, "r") as file:

        num_symbols = int(file.readline().strip())

        for line in file:
            weight = int (line.strip())
            weights.append(weight)

    return weights 

def huffman_length(weights):
    queque = []

    # Heapq for weights elements 
    for i, weight in enumerate(weights):
        heapq.heappush(queque, (weight, [i]))

    byte = [0] * len(weights)

    # Combine nodes until last weight 
    while len(queque) > 1:

        # Pop two smallest elements 
        weight_1, depth_1 = heapq.heappop(queque)
        weight_2, depth_2 = heapq.heappop(queque)

        # Creat new weight max + 1 or random + 1
        new_weight = weight_1 + weight_2


        for depth in depth_1 + depth_2:
            byte[depth] += 1

        # Push new weight 
        heapq.heappush(queque, (new_weight, depth_1 + depth_2))

    return byte
        

def main():

    weights = read_file("huffman.txt")

    length = huffman_length(weights)


    print(f"Maximum length:", max(length))
    print(f"Manimum length:", min(length))
    

if __name__ == "__main__":
    main()

# Output: (max: 19), (min: 9)