def remove_duplicates(s):

    hashset = set([])
    write_index = 0
    read_index = 0

    while s[read_index] != '\0':
        if s[read_index] not in hashset:
            hashset.add(s[read_index])
            s[write_index] = s[read_index]
            write_index += 1

        read_index += 1
    
    s[write_index] = '\0'