"""

재귀함수를 이용해 리스트 총합 구하기

"""

a = input().split()
total = 0


def test(n):
    global total
    if n < 1:
        return total
    total += int(a.pop())
    return test(n - 1)


result = test(len(a))
print(result)
