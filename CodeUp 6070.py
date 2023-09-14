# 월 입력받아 계절 출력하기

a = int(input())


"""if a // 3 == 1:
    print("spring")
elif a // 3 == 2:
    print("summer")
elif a // 3 == 3:
    print("fall")
else:
    print("winter")"""


# if 사용하지 않고 풀기
seasons = ["winter", "spring", "summer", "fall"]

result = seasons[(a % 12) // 3]

print(result)
