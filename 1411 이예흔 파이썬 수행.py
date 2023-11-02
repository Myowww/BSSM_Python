# 1번
def p(a):
    if a == 1:
        return 1
    print(a, end=" ")
    return p(a-1)


a = int(input())
print(p(a))


# 2번
total = 0
def sum(b):
    global total
    if not b:
        return total
    total = total + int(b.pop())
    return sum(b)


b = input().split()
test = sum(b)
print(test)


# 3번
max = 0
def find_Max(c):
    global max
    if not c:
        return max
    
    n = c.pop(0)
    if int(n) > int(max):
        max = n
        return find_Max(c)
    else: return find_Max(c)


c = input().split()
test = find_Max(c)
print(test)