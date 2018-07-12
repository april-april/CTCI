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

def test(v, val, expected):
    output = find_sum_of_two(v, val)
    print("exist(A, " + str(val) + ") = " + str(output) + "\n")
    assert expected == output

def main():
    v = [2, 1, 8, 4, 7, 3]
    test(v, 3, True)
    test(v, 20, False)
    test(v, 1, False)
    test(v, 2, False)
    test(v, 7, True)

main()


