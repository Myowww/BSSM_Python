global total


def test(n):
    global total
    total += n - 1
    if n > 1:
        test(n - 1)
    else:
        return total


total = 0
n = int(input())
print(test(n))
