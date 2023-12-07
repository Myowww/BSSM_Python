# 클래스 구현
class Queue:
    def __init__(self, capacity=5) -> None:
        self.capacity = capacity
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item) -> None:
        if not self.isFull():
            self.rear += 1
            self.list[self.rear] = item
            print(self.list)
        else:
            return "Queue is full"

    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
            temp = self.list[self.front]
            self.list[self.front] = None
            return temp
        else:
            return "Queue is empty"

    def peek(self):
        if self.isEmpty():
            return self.list[self.front + 1]
        else:
            return "Queue is empty"
