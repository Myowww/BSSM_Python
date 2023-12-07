def fac(n):
    if n > 1:
        return n + fac(n - 1)
    else:
        return 1


n = int(input())
max = fac(n)

for i in range(n):
    for j in range(i + 1):
        print(max, end=" ")
        max = max - 1
    print()
