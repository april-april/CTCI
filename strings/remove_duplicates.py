from array import array

def remove_duplicates(str):

    write_index = 0

    for i in range(len(str)):
        found = False


        for j in range(0, write_index):
            if str[i] == str[j]:
                found = True
                break

        
        if found == False:
            str[write_index] = str[i]
            write_index += 1
        
    str[write_index] = '\0'

    return str

def getArray(t):
    s = array('c', t)
    s.append('\0')
    print s
    return s

def main():
    test = 'aaaaabbbbccc'
    print remove_duplicates(getArray(test))
    print test
    
