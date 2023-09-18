def count(a, n):
    if n <= 0:
        return
    print(n)
    count(a, n - 1)


a = int(input())
count(a, a)
