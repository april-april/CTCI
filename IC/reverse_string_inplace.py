  def reverse(string):

    left_index  = 0
    right_index = len(string) - 1

    while left_index < right_index:
        # Swap characters
        string[left_index], string[right_index] = \
            string[right_index], string[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1