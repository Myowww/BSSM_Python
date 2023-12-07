n = int(input())

a1 = list(map(int, input().split()))

for i in range(n):
    print(*a1)
    a1.append(a1.pop(0))
