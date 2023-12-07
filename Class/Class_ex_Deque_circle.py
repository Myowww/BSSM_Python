class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.list = [None] * capacity

    # 덱이 비었는가?
    def isEmpty(self):
        return self.front == self.rear

    # 덱이 가득 찼는가?
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    # 덱의 앞에 추가하기
    def Addfront(self, e):
        if self.isFull():
            print("덱이 가득찼습니다")
            return None

        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.list[self.front] = e

    # 덱의 끝에 추가하기
    def Addrear(self, e):
        if self.isFull():
            print("덱이 가득찼습니다")
            return None

        self.list[self.rear] = e
        self.rear = (self.rear + 1) % self.capacity

    # 덱의 앞 지우기
    def Deletefront(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None

        self.front = (self.front + 1) % self.capacity
        return self.list[self.front]

    # 덱의 끝 없애기
    def Deleterear(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None

        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return self.list[self.rear]

    # 덱의 앞 조회하기
    def Getfront(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None
        return self.list[self.front]

    # 덱의 끝 조회하기
    def Getrear(self):
        if self.isEmpty():
            print("덱이 비었습니다")
            return None
        return self.list[(self.rear - 1 + self.capacity) % self.capacity]


deque = Deque()

# 앞쪽에 원소 추가
for i in range(1, 3):
    deque.Addfront(i)
    print(f"덱 앞쪽에 {i} 추가: {deque.list}")

# 뒤쪽에 원소 추가
for i in range(3, 6):
    deque.Addrear(i)
    print(f"덱 뒤쪽에 {i} 추가: {deque.list}")

# 앞쪽 원소 확인
print(f"덱 앞쪽 원소 확인: {deque.Getfront()}")

# 뒤쪽 원소 확인
print(f"덱 뒤쪽 원소 확인: {deque.Getrear()}")

# 앞쪽에서 원소 삭제
for i in range(2):
    print(f"덱 앞에서 {deque.Deletefront()} 삭제: {deque.list}")

# 뒤쪽에서 원소 삭제
for i in range(2):
    print(f"덱 뒤에서 {deque.Deleterear()} 삭제: {deque.list}")
