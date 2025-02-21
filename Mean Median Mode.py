import statistics

# Define the list
data = [5, 1, 8, 2, 5, 3, 9, 1, 5, 6]

# Calculate mean
mean = statistics.mean(data)
print("Mean:", mean)

# Calculate median
median = statistics.median(data)
print("Median:", median)

# Calculate mode
mode = statistics.mode(data)
print("Mode:", mode)

# Define the list
data = [5, 1, 8, 2, 5, 3, 9, 1, 5, 6]

# Calculate mean
def calculate_mean(data):
    return sum(data) / len(data)

mean = calculate_mean(data)
print("Mean:", mean)

# Calculate median
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:  # If even number of elements
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:  # If odd number of elements
        return sorted_data[mid]

median = calculate_median(data)
print("Median:", median)

# Calculate mode
def calculate_mode(data):
    frequency = {}
    
    # Count the frequency of each element in the list
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    
    # Find the maximum frequency
    max_count = max(frequency.values())
    
    # Find the elements with the maximum frequency
    modes = [key for key, count in frequency.items() if count == max_count]
    
    # If there are multiple modes, return the first one (based on the requirement)
    return modes[0]

mode = calculate_mode(data)
print("Mode:", mode)
