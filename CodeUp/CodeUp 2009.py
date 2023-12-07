k, n = map(int, input().split())
coffee = 0

while k > n - 1:
    k -= n
    coffee += 1
    k += 1

print(coffee)
