a = list(map(int, input()))
count = sum(a)

while count >= 10:
    # 리스트 컴프리헨션
    a = [int(digit) for digit in str(count)]
    count = sum(a)

print(count)
