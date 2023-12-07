# 나만의 스택 ADT 만들기

"""
1. isEmpty
2. isFull
3. 스택의 맨 위에 삽입 : push(e)
4. 맨 위의 요소 삭제 : pop()
5. 맨 위의 요소 반환 : peek()

---

나만의 ADT

6. 스택 값 전부 삭제 : allPop()
7. 스택 값 전부 출력 : allPrint()
8. 스택 값 역순 출력 : backPrint()

---

0. 프로그램 종료 : exit

"""


# STACKADT 선언
class StackADT:
    # init
    def __init__(self):
        self.size = 10
        self.list = [None] * self.size
        self.top = -1

    # 스택이 비었는 지 확인
    def isEmpty(self):
        # top이 -1이면 비어있음
        if self.top == -1:
            return True
        else:
            return False

    # 스택이 가득 찼는 지 확인
    def isFull(self):
        # top이 (스택의 사이즈 - 1) 면 가득 참
        if self.top == self.size - 1:
            return True
        else:
            return False

    # 스택에 값 채우기
    def push(self, e):
        # 스택이 가득 찼으면 채우지 않음
        if self.isFull() == True:
            print("배열이 가득 찼습니다")
            return 0

        # top을 1 올리고 top에 값을 채움
        self.top += 1
        self.list[self.top] = e

    # 스택에 요소 없애기
    def pop(self):
        # 스택이 비었으면 없애지 않음
        if self.isEmpty() == True:
            print("배열이 텅 비었습니다")
            return 0

        # 터트릴 요소를 출력하고 None으로 바꿈
        # top을 1 낮추어 한 칸이 다시 비었음을 뜻함
        print(self.list[self.top], end=" ")
        self.list[self.top] = None
        self.top -= 1

    # 스택의 맨 위의 값을 반환
    def peek(self):
        # 스택의 맨 위(top)의 값 출력
        print(self.list[self.top])

    # 스택의 모든 요소 터트리기
    def allPop(self):
        # 스택이 비었으면 터트리지 않음
        if self.isEmpty() == True:
            return

        # (top + 1)만큼 pop() 반복
        for i in range(0, self.top + 1):
            self.pop()

    # 스택 모든 요소 출력
    def allPrint(self):
        # 스택이 비었으면 출력하지 않음
        if self.isEmpty() == True:
            return

        # 스택의 사이즈만큼 반복
        for i in range(self.size):
            # i가 None(빈칸)일 때 반복 중지
            if self.list[i] == None:
                return

            # 스택의 i번째 값 출력
            # 줄바꿈 없이 띄어쓰기로 이음
            print(self.list[i], end=" ")

    # 스택 역순 출력
    def backPrint(self):
        # 스택을 역순으로 정렬한 data 생성
        data = self.list[: self.top + 1]

        # data 출력
        for i in reversed(data):
            # i가 None(빈칸)일 때 반복 중지
            if i is None:
                return
            # 스택의 i번째 값 출력
            # 줄바꿈 없이 띄어쓰기로 이음
            print(i, end=" ")

    # 스택 종료문구 출력
    def exit(self):
        print("종료합니다")


# ----------------------------------------------------------
# Main

s = StackADT()

print("1. push()")
print("2. pop()")
print("3. peek()")
print("4. allPop()")
print("5. allPrint()")
print("6. backPrint()")
print("0. exit()")

while 1:
    a = input("\n명령 입력 : ")
    if a == "1":
        n = int(input("삽입할 수를 입력해주세요 : "))
        s.push(n)

    elif a == "2":
        s.pop()

    elif a == "3":
        s.peek()

    elif a == "4":
        s.allPop()

    elif a == "5":
        s.allPrint()

    elif a == "6":
        s.backPrint()

    elif a == "0":
        s.exit()
        break
