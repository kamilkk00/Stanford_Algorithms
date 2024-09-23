def file(file_name):
    jobs = []
    with open(file_name, "r") as file:

        # Fist line contains the number of job 
        next(file)
        for line in file: 
            data = list(map(int, line.split()))
            jobs.append(data)
    return jobs

def sorting(jobs):
    # Sort jobs by difference 
    sorted_jobs = sorted(jobs, key=lambda x: (x[0] - x[1], x[0]), reverse=True )
    return sorted_jobs

def optimal_sorting(jobs):
    # Sort by ratio weight/length 
    sorted_jobs = sorted(jobs, key=lambda x: (x[0]/x[1], x[0]), reverse= True)
    return sorted_jobs

def calculate(sorted):
    current_time = 0 
    weighted_sum = 0 

    for job in sorted:
        current_time += job[1]
        weighted_sum += job[0] * current_time 

    return weighted_sum

def main():
    jobs = file("jobs.txt")
    sorted = sorting(jobs)
    time = calculate(sorted)
    optimal_sorted = optimal_sorting(jobs)
    optimal_time = calculate(optimal_sorted)
    print("Output 1:", time)
    print("Output 2:", optimal_time)

if __name__ == "__main__":
    main()

# Output_1: 69119377652
# Output_2: 67311454237