def odd(a, b):
    if a > b:
        return
    if a % 2 == 1:
        print(a)

    odd(a + 1, b)


a, b = map(int, input().split())
odd(a, b)
