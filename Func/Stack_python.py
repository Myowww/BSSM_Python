# 스택 ADT

# push(e) : 요소 e를 스택의 맨 위에 추가
# pop() : 스택의 맨 위에 있는 요소를 꺼내 반환한다.
# isEmpty() : 스택이 비어있는 true를 아니면 false를 반환한다.
# isFull() : 스택이 가득 차 있으면 true를 아니면 false를 반환한다.
# peek() : 스택의 맨 위에 있는 항목을 삭제하지 않고 반환한다.

stack_size = 5
list = [None] * stack_size
top = -1


def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False


def isFull():
    global top
    if top == stack_size - 1:
        return True
    else:
        return False


def push(e):
    global top

    if isFull() == True:
        print("배열이 가득 찼습니다")
        return 0

    top += 1
    list[top] = e


def pop():
    global top

    if isEmpty() == True:
        print("배열이 텅 비었습니다")
        return 0

    print(list[top])
    list[top] = None
    top -= 1


def peek():
    global top
    print(list[top])


print("push 확인")
push(1)
push(2)
push(3)
push(4)
push(5)

print(list)

push(5)

print("pop 확인")
pop()
pop()
pop()
pop()
pop()
pop()

print("peek 확인")
push(6)
print(list)
peek()

print(list)

"""

오늘 수업에서 알게된 점
함수에서 True나 False 값을 반환할 때, 

if 함수 == True:
로 쓰면 반환값이 적용되지 않는다!

if 함수() == True:
로 써야 함수의 반환값이 True인지 if문이 적용됨.

Ex.
def isFull():
    global top
    if top == stack_size - 1:
        return True
    else:
        return False


def push(e):
    global top

    if isFull == True:      # 여기서 ()가 없기 때문에 반환값이 True인지 확인 X
        print("배열이 가득 찼습니다")
        return 0

    top += 1
    list[top] = e

"""
