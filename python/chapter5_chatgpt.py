from collections import Counter

def appearxtimes(*args):
    # Check if the input has at least two elements
    if len(args) < 2:
        return -1
    
    # Extract the required number of times
    x = args[0]
    
    # Count the occurrences of each integer
    count_dict = Counter(args[1:])
    
    # Get a list of integers that appear x times
    x_times_integers = [k for k, v in count_dict.items() if v == x]
    
    # If there are no integers that appear x times, return -1
    if not x_times_integers:
        return -1
    
    # Return the smallest integer that appears x times
    return min(x_times_integers)

# Example 1
result = appearxtimes(2, 1, 2, 3, 2, 4, 1, 5, 6, 5)
print(result) 

# Example 2
result = appearxtimes(3, 1, 2, 3, 4, 5, 6)
print(result)

# Example 3
result = appearxtimes(2, 1, 2, 3, 3, 4, 4, 5, 5)
print(result)