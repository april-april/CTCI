#time: O(n), space: O(n)
def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # no duplicate
    raise Exception('no duplicate!')

#time O(n^2), space O(1)
def find_repeat_brute_force(numbers):
    for needle in range(1, len(numbers)):
        has_been_seen = False
        for number in numbers:
            if number == needle:
                if has_been_seen:
                    return number
                else:
                    has_been_seen = True

    # no duplicate
    raise Exception('no duplicate!')


#Optimize for better space and time



