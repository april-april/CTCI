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
        if self.empty():
            raise Empty

        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                val = self.stack1[-1]
                self.stack1.pop()
                self.stack2.append(val)

        val = self.stack2[-1]
        self.stack2.pop()
        return val

def main():
    q1 = queue_using_stack()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print q1.dequeue()

    q1.enqueue(4)
    print q1.dequeue()
    print q1.dequeue()
    print q1.dequeue()

main()