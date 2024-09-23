import heapq

max_heap = []
min_heap = []

def read_file():
    with open("median.txt", "r") as file:
        for line in file:
            number = int(line.strip())
            yield number 

def add_number(number, max_heap, min_heap):
    
    # Adding first or smaller element to max_heap 
    if len(max_heap) == 0 or number <= -max_heap[0]:
        heapq.heappush(max_heap, -number)

    # Adding other element to min_heap
    else: 
        heapq.heappush(min_heap, number)

    # If max_heap have more element, move largest to min_heap
    if len(max_heap) > len(min_heap) + 1: 
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

def median(max_heap, min_heap):

    # If length of max_heap >= of min_heap, then the median is the largest element in max_heap 
    if len(max_heap) >= len(min_heap):
        return -max_heap[0]

def median_sum(median, total_sum):

    # Add current median to total sum 
    total_sum += median 

    # Apply modulo 10000 to reduce total sum 
    total_sum %= 10000

    return total_sum

def main():
    total_sum = 0 

    for number in read_file():
        add_number(number, max_heap, min_heap)
        current_median = median(max_heap, min_heap)
        total_sum = median_sum(current_median, total_sum)

    print(total_sum)

if __name__ == "__main__":
    main()

# Output: 1213