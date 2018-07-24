#breadth first search
import collections

def breadth_first_search(graph, root):

    seen, queue = set(), collections.deque([root])

    while queue: 

        vertex = queue.popleft()
        
        for neighbour in graph[vertex]:
            if neighbour not in seen: 
                seen.add(neighbour) 
                queue.append(neighbour)
                print(seen)
                
    return seen 


if __name__ == '__main__':
    graph = {0: [1, 2, 3], 1: [2], 2: [], 3: []} 
    breadth_first_search(graph, 0)


