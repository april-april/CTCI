#top-down approach to multiple numbers in a range, recursion

def product_1_to_n(n):
    # We assume n >= 1
    return n * product_1_to_n(n - 1) if n > 1 else 1