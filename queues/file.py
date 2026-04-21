class Queue:
    def __init__(self, length):
        self.arr = [0] * length
        self.front = -1
        self.rear = -1
        self.size = length

    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.arr[self.rear] = value

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return

        item = self.arr[self.front]
        self.front += 1
        return item

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Empty queue")
        else:
            print(self.arr[self.front:self.rear+1])


q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Removed:", q.dequeue())

q.display()