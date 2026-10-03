class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        self.queue.pop(0)

    def printQ(self):
        print(self.queue)

dmo = Queue()


dmo.enqueue(45)
dmo.enqueue(23)
dmo.enqueue(32)
dmo.enqueue(1)

dmo.printQ()

dmo.dequeue()

dmo.printQ()