def read_file(file_name):
    weights = []
    with open(file_name, "r") as file:
        
        x = int(file.readline().strip())

        for line in file: 
            weight = int(line.strip())
            weights.append(weight)

    weights.insert(0, 0)
    return weights

def max_weight(weights):
    n = len(weights) - 1
    A = [0] * (n + 1)

    A[0] = 0 
    A[1] = weights[1]
    

    for i in range (2, n + 1):
        A[i] = max(A[i - 1], A[i - 2] + weights[i])        

    return A

def mwis(weights, A):
    mwis = [] 

    i = len(weights) - 1

    # If vertex is part of MWIS 
    while i >= 1:
        if i == 1:
            if A[1] == weights[1]:
                mwis.append(1)
                i -= 1  
        else:   
            if A[i] == A[i - 2] + weights[i]:
                mwis.append(i)
                i -= 2
            else: 
                i -= 1

    return mwis

def check_vertices(mwis, vertices):
    result = []

    for vertex in vertices: 
        if vertex in mwis:
             result.append(1)
        else:
            result.append(0)
    return result 

def main():
    weights = read_file("mwis.txt")

    A = max_weight(weights)

    mwis_set = mwis(weights, A)

    vertices_check = [1, 2, 3, 4, 17, 117, 517, 997]

    result = check_vertices(mwis_set, vertices_check)

    bit_string = ''.join(map(str, result))


    print (bit_string)


if __name__ == "__main__":
    main()

# Output: 10100110