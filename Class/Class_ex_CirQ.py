class CircleQueue:
    # 생성자 함수로, 원형 큐를 초기화합니다.
    def __init__(self, size=5):
        self.size = size  # 큐의 크기
        self.list = [None] * size  # 큐의 요소들을 저장할 리스트
        self.front = 0  # 큐의 front 위치를 가리킵니다.
        self.rear = 0  # 큐의 rear 위치를 가리킵니다.

    # 큐가 비어있는지 확인하는 함수입니다.
    def isEmpty(self):
        return self.rear == self.front  # rear와 front가 같으면 큐가 빈 것입니다.

    # 큐가 가득 찼는지 확인하는 함수입니다.
    def isFull(self):
        return (
            self.rear + 1
        ) % self.size == self.front  # rear + 1을 큐의 크기로 나눈 나머지가 front와 같다면 큐가 가득 찬 것입니다.

    # 큐에 요소를 추가하는 함수입니다.
    def enQueue(self, item):
        if not self.isFull():  # 큐가 가득 차지 않았다면
            self.rear = (self.rear + 1) % self.size  # rear 위치를 하나 뒤로 이동시킵니다.
            self.list[self.rear] = item  # 새로운 요소를 추가합니다.
            print(self.list)  # 큐의 상태를 출력합니다.
        else:
            print("Queue is full")  # 큐가 가득 찼다면 메시지를 출력합니다.

    # 큐에서 요소를 제거하는 함수입니다.
    def deQueue(self):
        if not self.isEmpty():  # 큐가 비어있지 않다면
            self.front = (self.front + 1) % self.size  # front 위치를 하나 뒤로 이동시킵니다.
            self.list[self.front] = None  # 제거된 위치의 요소를 None으로 설정합니다.
            print(self.list)  # 큐의 상태를 출력합니다.
        else:
            print("Queue is empty")  # 큐가 비어 있다면 메시지를 출력합니다.

    # 큐의 맨 앞 요소를 반환하는 함수입니다.
    def peek(self):
        if not self.isEmpty():  # 큐가 비어있지 않다면
            return self.list[(self.front + 1) % self.size]  # front 다음 위치의 요소를 반환합니다.
        else:
            print("Stack is Empty!")  # 큐가 비어 있다면 메시지를 출력합니다.

    # 큐의 모든 요소를 출력하는 함수입니다.
    def print_all(self):
        temp = [i for i in self.list if i is not None]  # None이 아닌 요소들만 저장합니다.
        print(temp)  # 저장된 요소들을 출력합니다.

    # 큐의 요소들을 역순으로 출력하는 함수입니다.
    def print_reverse(self):
        temp = [i for i in self.list if i is not None]  # None이 아닌 요소들만 저장합니다.
        print(temp[::-1])  # 저장된 요소들을 역순으로 출력합니다.

    # 큐의 모든 요소를 제거하는 함수입니다.
    def clear(self):
        while not self.isEmpty():  # 큐가 비어있지 않다면
            self.deQueue()  # deQueue 함수를 호출하여 요소를 제거합니다.


from random import randint

q_size = 5  # 큐의 크기를 설정합니다.

# CircleQueue 클래스의 인스턴스를 생성합니다.
q = CircleQueue(q_size)

# 큐에 랜덤한 정수를 추가합니다.
print("큐에 요소 추가")
for i in range(q_size):
    q.enQueue(randint(1, 100))

# 큐의 모든 요소를 출력합니다.
print("큐 모두 출력")
q.print_all()

# 큐의 요소들을 역순으로 출력합니다.
print("큐 역순으로 출력")
q.print_reverse()

# 큐의 맨 앞 요소를 확인합니다.
print("큐의 맨 앞 요소 확인")
print(q.peek())

# 큐에서 요소를 제거합니다.
print("큐에서 요소 제거")
print(q.deQueue())
print(q.deQueue())

# 큐의 모든 요소를 제거합니다.
print("큐의 모든 요소 제거")
q.clear()
q.print_all()
