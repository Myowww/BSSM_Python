def money(a, num):
    if a > 50000:
        a -= 50000
        num += 1

    if a > 10000:
        a -= 10000
        num += 1

    if a > 5000:
        a -= 5000
        num += 1

    if a > 1000:
        a -= 1000
        num += 1

    if a > 500:
        a -= 500
        num += 1

    if a > 100:
        a -= 100
        num += 1

    if a > 50:
        a -= 50
        num += 1

    if a > 10:
        a -= 10
        num += 1

    if a == 0:
        return num

    return money(a, num)


a = input()
a = int(a)
num = 0

print(money(a, num))
