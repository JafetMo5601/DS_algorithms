class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(-1)
        else:
            print("The queue is empty!")

    def isEmpty(self):
        return len(self.queue) > 0

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[-1]

    def printQueue(self):
        print(self.queue)

queue = Queue()

queue.printQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.printQueue()
queue.dequeue()
print(queue.front())
print(queue.rear())
queue.printQueue()
