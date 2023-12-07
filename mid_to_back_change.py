# 중위수식을 후위수식으로 바꾸기


class StackADT:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, e):
        if self.isFull():
            print("배열이 가득 찼습니다")
            return 0
        self.top += 1
        self.list[self.top] = e

    def pop(self):
        if self.isEmpty():
            print("배열이 텅 비었습니다")
            return 0
        popped_value = self.list[self.top]
        self.list[self.top] = None
        self.top -= 1
        return popped_value

    def peek(self):
        return self.list[self.top]


def precedence(op):
    if op in ("(", ")"):
        return 0
    elif op in ("+", "-"):
        return 1
    elif op in ("*", "/"):
        return 2
    else:
        return -1


def infix_to_postfix(expression):
    stack = StackADT(100)
    output = []

    for term in expression:
        if term == "(":
            stack.push("(")
        elif term == ")":
            while not stack.isEmpty() and stack.peek() != "(":
                op = stack.pop()
                output.append(op)
            stack.pop()  # Pop the remaining "("

        elif term in "+-*/":
            while not stack.isEmpty() and precedence(stack.peek()) >= precedence(term):
                op = stack.pop()
                output.append(op)
            stack.push(term)

        else:
            output.append(term)

    while not stack.isEmpty():
        output.append(stack.pop())

    return "".join(output)


infix1 = input()
postfix1 = infix_to_postfix(infix1)
print(postfix1)
