#Implement a queue using Stacks.
#use 2 stacks
class queue_using_stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def dequeue(self):