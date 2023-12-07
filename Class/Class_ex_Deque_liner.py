class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.list = [None] * capacity

    # 덱이 비었는가?
    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    # 덱이 가득 찼는가?
    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    # 덱의 앞에 추가하기
    def Addfront(self, e):
        if self.isFull():
            print("덱이 가득찼습니다")
            return None

        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity

        self.list[self.front] = e

    # 덱의 끝에 추가하기
    def Addrear(self, e):
        if self.isFull():
            print("덱이 가득찼습니다")
            return None

        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.list[self.rear] = e

    def Deletefront(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None

        deleted_element = self.list[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return deleted_element

    def Deleterear(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None

        deleted_element = self.list[self.rear]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

        return deleted_element

    def Getfront(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None

        return self.list[self.front]

    def Getrear(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None

        return self.list[self.rear]


deque = Deque()

for i in range(1, 3):
    deque.Addfront(i)
    print(f"덱 앞쪽에 {i} 추가: {deque.list}")

for i in range(3, 6):
    deque.Addrear(i)
    print(f"덱 뒤쪽에 {i} 추가: {deque.list}")

print(f"덱 앞쪽 원소 확인: {deque.Getfront()}")
print(f"덱 뒤쪽 원소 확인: {deque.Getrear()}")

for i in range(2):
    print(f"덱 앞에서 {deque.Deletefront()} 삭제: {deque.list}")

for i in range(2):
    print(f"덱 뒤에서 {deque.Deleterear()} 삭제: {deque.list}")
