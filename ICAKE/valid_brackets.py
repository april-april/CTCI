  def is_valid(code):
    openers_to_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }
    openers = set(openers_to_closers.keys())
    closers = set(openers_to_closers.values())

    openers_stack = []
    for char in code:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()
                # If this closer doesn't correspond to the most recently
                # seen unclosed opener, short-circuit, returning False
                if not openers_to_closers[last_unclosed_opener] == char:
                    return False

    return openers_stack == []