pasta = []
juice = []

for _ in range(3):
    value = int(input())
    pasta.append(value)

for _ in range(2):
    value = int(input())
    juice.append(value)

pm = min(pasta)
jm = min(juice)

price = pm + jm + ((pm + jm) * (10 / 100))

print(price)
