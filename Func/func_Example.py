# list_sum을 재귀함수로 표현
def list_sum(l1):
    if not l1:
        return 0
    return l1.pop() + list_sum(l1)


# list_print를 재귀함수로 표현
def list_print(l1):
    if not l1:
        return
    print(l1.pop(0))
    list_print(l1)


# 역순출력을 재귀함수로 표현
def list_Bprint(l1):
    if not l1:
        return
    print(l1.pop())
    list_Bprint(l1)


# list_reverse 재귀함수로 구현
def list_reverse(l1):
    if not l1:
        return []
    return [l1[-1]] + list_reverse(l1[:-1])


# list_times(곱하기) 재귀함수로 구현
def list_times(l1):
    if not l1:
        return 1
    return l1.pop() * list_times(l1)


# lsit_pop 재귀함수로 구현
def list_pop(l1):
    if not l1:
        return None
    elif len(l1) == 1:
        return l1[0]
    else:
        return list_pop(l1[1:])


# 2차원 배열 1차원 배열로 만들기
def list_flatten(l1):
    result = []
    for i in l1:
        if type(i) == list:
            result += list_flatten(i)
        else:
            result += [i]
    return result


# pop함수 구현
def list_pop2(l1):
    if not l1:
        return None

    last_item = l1[-1]
    del l1[-1]

    return last_item


def main():
    l1 = [1, 2, 3, 4, 5]
    print(list_sum(l1))
    print()

    l1 = [1, 2, 3, 4, 5]
    list_print(l1)
    print()

    l1 = [1, 2, 3, 4, 5]
    list_Bprint(l1)
    print()

    l1 = [1, 2, 3, 4, 5]
    print(list_reverse(l1))
    print()

    l1 = [1, 2, 3, 4, 5]
    print(list_times(l1))

    l1 = [1, 2, 3, 4, 5]
    print(list_pop(l1))
    print()

    l1 = [[1, 2], [3, 4], [5]]
    print(list_flatten(l1))

    l1 = [1, 2, 3, 4, 5]
    print(list_pop2(l1))
    print(l1)


main()


# def addList(argList: list):
#     _sum = 0
#     for num in argList:
#         _sum = _sum + num

#     return _sum


# result = addList([1, 2, 3, 4, 5])
# print(result)
