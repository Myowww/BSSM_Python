# 덱(Deque)ADT

# isEmpty() : 덱이 비어있으면 true를 아니면 false를 반환한다.
# isFull() : 덱이 가득 차 있으면 true를 아니면 false를 반환한다.
# Addfront(e) : 맨 앞(전단)에 새로운 요소 e를 추가한다.
# Deletefront() : 맨 앞(전단)의 요소를 꺼내서 반환한다.
# Getfront() : 맨 앞(전단)의 요소를 꺼내지 않고 반환한다.
# Addrear(e) : 맨 뒤(후단)에 새로운 요소e를 추가한다.
# Deleterear() : 맨 뒤(후단)의 요소를 꺼내서 반환한다.
# Getrear() : 맨 뒤(후단)의 요소를 꺼내지 않고 반환한다.


deque_size = 5
list = [None] * deque_size
front = rear = 0


def isEmpty():
    global front, rear
    if front == rear:
        return True
    else:
        return False


def isFull():
    global front, rear
    if (rear + 1) % deque_size == front:
        return True
    else:
        return False


def Addfront(e):
    global front, rear
    if isFull(front, rear, deque_size) == 1:
        return 0
    list[rear] = e
    rear = (rear + 1) % deque_size


def Deletefront():
    global front, rear
    if isEmpty(front, rear) == 1:
        return 0
    front = (front + 1) % deque_size
    return list[(front - 1) % deque_size]


def Getfront():
    global front, rear
    if isEmpty(front, rear) == 1:
        return 0
    front = (front + 1) % deque_size


def Addrear(e):
    global front, rear
    if isFull(front, rear, deque_size) == 1:
        return 0
    rear += 1
    list[rear] = e


def Deleterear():
    global front, rear
    if isEmpty(front, rear) == 1:
        return 0
    print(list[rear])
    list[rear] = None
    rear -= 1


def Getrear():
    global rear
    print(list[rear])
