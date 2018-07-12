# find_sum_of_two function return true if
# there are two values in array who
# sum to value and returns false otherwise

def find_sum_of_two(array, val):
    found_values = set()
    for a in array:
        if val - a in found_values:
            return True
        
        found_values.add(a)
    
    return False

