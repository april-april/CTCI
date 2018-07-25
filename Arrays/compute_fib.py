def compute_fib(n):
2	    list = [0,1]
3	
4	    prev = 0
5	    curr = 1
6	
7	    for num in range(n - 2):
8	        list.append(prev + curr)
9	        
10	        temp = prev + curr 
11	        prev = curr 
12	        curr = temp
13	    
14	compute_fib(5)