def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(gcd(a, gcd(b, c)))
