#Implement a stack using Queues.
import collections

class stack_using_queue:
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, data):
        self.queue1.append(data)