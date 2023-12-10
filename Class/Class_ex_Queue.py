# 클래스 구현
class Queue:
    # init
    def __init__(self, size=5) -> None:
        self.size = size
        self.list = [None] * size
        self.front = 0
        self.rear = 0

    # 큐가 비었는 지 확인
    def isEmpty(self):
        # front와 rear가 같으면 큐가 빔 -> True 반환
        # 아니면 False 반환
        return self.front == self.rear

    # 큐가 다 찼는 지 확인
    def isFull(self):
        # rear가 size와 같다면 가득 참 -> True 반환
        # 아니면 False 반환
        return self.rear == self.size

    # 큐에 원소 삽입
    def enqueue(self, item):
        # 큐가 가득 차지 않았다면
        if not self.isFull():
            # rear의 위치에 원소 삽입
            self.list[self.rear] = item
            # rear에 1 더함
            self.rear += 1
            # 큐 출력
            print(self.list)
        # 아니면 큐가 가득 찼음 -> 메시지 출력
        else:
            return "Queue is full"

    # 큐의 원소 삭제
    def dequeue(self):
        # 큐가 비어있지 않다면
        if not self.isEmpty():
            # temp의 값을 front의 위치에 있는 원소로 지정
            temp = self.list[self.front]
            # front의 위치에 있는 값을 None으로 변경
            self.list[self.front] = None
            # front에 1 더함
            self.front += 1
            # 원래 있던 값(temp)을 반환
            return temp
        # 아니면 큐가 비어있음 -> 메시지 출력
        else:
            return "Queue is empty"

    # 큐의 맨 앞의 요소 반환
    def peek(self):
        if not self.isEmpty():  # 만약 큐가 비어있다면
            return self.list[self.front]
        else:
            return "Queue is empty"

    # 큐 모든 요소 터트리기
    def clear(self):
        while not self.isEmpty():
            self.dequeue()

    # 큐 역순으로 출력
    def print_reverse(self):
        temp = [i for i in self.list if i is not None]
        print(temp[::-1])

    # 큐 모두 출력
    def print_all(self):
        temp = [i for i in self.list if i is not None]
        print(temp)

    # 큐 출력 Type을(를) 정하여 정렬하여 출력
    def print_sort(self, sortType):
        temp = [i for i in self.list if i is not None]

        if sortType == 0:  # 오름차순
            temp = sorted(temp)
            return temp

        elif sortType == 1:  # 내림차순
            temp = sorted(temp, reverse=True)
            return temp

        else:
            return "Invalid type"


from random import randint

q_size = 5

# 클래스 인스턴스 생성
q = Queue(q_size)

# enqueue: 큐에 요소 추가
print("큐에 요소 추가")
for i in range(q_size):
    q.enqueue(randint(1, 100))  # [10, None, None, None, None]

# print_all: 큐 모두 출력
print("큐 모두 출력")
q.print_all()

# print_reverse: 큐 역순으로 출력
print("큐 역순으로 출력")
q.print_reverse()

# print_sort: 큐 출력 Type을(를) 정하여 정렬하여 출력
print("큐 오름차순 출력")
print(q.print_sort(0))
print("큐 내림차순 출력")
print(q.print_sort(1))

# peek: 큐의 맨 앞 요소 확인
print("큐의 맨 앞 요소 확인")
print(q.peek())  # 30 출력

# dequeue: 큐에서 요소 제거
print("큐에서 요소 제거")
print(q.dequeue())  # 10 출력, [None, 20, 30, None, None]
print(q.dequeue())  # 20 출력, [None, None, 30, None, None]

# allPop: 큐의 모든 요소 제거
print("큐의 모든 요소 제거")
q.clear()  # 30 출력 후, [None, None, None, None, None]
q.print_all()
