a = input()
reversed_a = a[::-1]
tot = 0

for i in range(0, len(reversed_a)):
    tot += int(reversed_a[i])

print(int(reversed_a))
print(tot)
