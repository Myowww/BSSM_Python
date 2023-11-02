a = input()
reversed_a = int(a[::-1])

tot = str(int(a) + reversed_a)
reversed_tot = tot[::-1]

if tot == reversed_tot:
    print("YES")
else:
    print("NO")
