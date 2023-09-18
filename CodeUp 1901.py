n = 1


def count(a):
    global n

    if n > a:
        return

    print(n)
    n = n + 1

    count(a)


a = int(input())
count(a)
