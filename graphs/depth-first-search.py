#stack-city

def dfs(graph, start):

    visited, stack = [], [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - set(visited))
        
        print(str(visited))

    return visited
