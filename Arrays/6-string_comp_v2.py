def string_compression(regular_string):
    
    compressed_string = []
    last_char = ""
    char_count = 0

    for char in regular_string:
        if char == last_char:
            char_count += 1
        else:
            if last_char != "":
                compressed_string.append(last_char + str(char_count))
            char_count = 1
        last_char = char            
    #final write
    compressed_string.append(last_char + str(char_count))
    compressed_string = "".join(compressed_string)

    if len(compressed_string) < len(regular_string):
        return compressed_string
    
    return regular_string
        
if __name__ == "__main__":
    test_string = 'aaaassd'
    print(string_compression(test_string))
