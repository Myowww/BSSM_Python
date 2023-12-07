q_size = 5
front = rear = 0


def enqueue(e, list):
    if isFull(front, rear, q_size) == 1:
        return 0
    list[rear] = e
    rear = (rear + 1) % q_size


def dequeue(list):
    if isEmpty(front, rear) == 1:
        return 0
    front = (front + 1) % q_size
    return list[(front - 1) % q_size]


def isEmpty(front, rear):
    if front == rear:
        return 1
    else:
        return 0


def isFull(front, rear, q_size):
    if (rear + 1) % q_size == front:
        return 1
    else:
        return 0


def peek(list):
    if isEmpty(front, rear) == 1:
        return 0
    front = (front + 1) % q_size


list = [0] * q_size

enqueue(1, list)
enqueue(2, list)
enqueue(3, list)
enqueue(4, list)
enqueue(5, list)
enqueue(6, list)

dequeue(list)
dequeue(list)
dequeue(list)
dequeue(list)
dequeue(list)
dequeue(list)

enqueue(6, list)
peek(list)
