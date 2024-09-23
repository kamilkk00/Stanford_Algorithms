def read_data(file_path):
    with open(file_path, 'r') as f:
        data = list(map(int, f.readlines()))
    return list(set(data))  


def hash_table(delta):
    h = {}

    # Hash table with keys -delta to delta 
    for i in range(-delta, delta + 1):
        h[i] = []
    return h


def buckets(data, h, delta):

    # Groups into buckets 
    for i in data:
        h[i // 10000].append(i)
    return h


def sum(h, delta, target_range=(-10000, 10000)):
    t = set()  
    for i in range(-delta, delta + 1):
        if len(h[i]) > 0:

            # Combines neigbhoring buckets with current one 
            find = h.get(-i-2, []) + h.get(-i-1, []) + h.get(-i, []) + h.get(-i+1, [])
            for x in h[i]:
                for y in find:
                    if x != y and target_range[0] <= x + y <= target_range[1]:
                        t.add(x + y)
    return len(t)


def main():
    file_path = "data.txt"  
    delta = 9999999
    target_range = (-10000, 10000)
    
    data = read_data(file_path)
    h = hash_table(delta)
    h = buckets(data, h, delta)
    result = sum(h, delta, target_range)
    print(result)

if __name__ == "__main__":
    main()

# Output: 427 