def sum_recursion(list):

    if len(list) <= 1:
        return list[0]
    else:
        result = list[0] + sum_recursion(list[1:])
        
    return result



def main():
    test = [1, 2, 3, 4, 5]
    print(sum_recursion(test))

main()

