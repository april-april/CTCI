import collections

stack = collections.deque()
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
print stack
print stack.pop()
print stack

stack.appendleft(9)
stack.appendleft(10)
print stack
stack.popleft()
print stack