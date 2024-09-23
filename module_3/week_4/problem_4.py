import sys
sys.setrecursionlimit(10000)  

def read_file(file_name):
    items = []
    with open(file_name, "r") as file:
        size, items_number = map(int, file.readline().split())  
        for line in file:
            value, weight = map(int, line.split())  
            items.append((value, weight))
    return size, items_number, items

def knapsack(size, items, n, memo):
    if (n, size) in memo:
        return memo[(n, size)]
    if n == 0 or size == 0:
        return 0
    value, weight = items[n - 1]
    result = knapsack(size, items, n - 1, memo) if weight > size else max(
        knapsack(size, items, n - 1, memo),
        value + knapsack(size - weight, items, n - 1, memo)
    )
    memo[(n, size)] = result
    return result

def main():
    #size, items_number, items_list = read_file("knapsack_1.txt")
    size, items_number, items_list = read_file("knapsack_big.txt")
    
    memo = {}
    result = knapsack(size, items_list, items_number, memo)
    print("Optimal value:", result)

if __name__ == "__main__":
    main()

# Output: 1: 249389 big: 4243395