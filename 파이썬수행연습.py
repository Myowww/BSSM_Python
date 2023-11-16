# 1278 자릿수 계산

# n = input()
# print(len(n))

""" 

파이썬에는 문자열의 길이를 구하는 len() 이라는 함수가 잇다.... 
삽질 왕왕햇음 ㅜ.ㅜ

"""

# 1361 별계단 만들기

# n = int(input())

# print("**")

# for i in range(1, n):
#     for j in range(i):
#         print(" ", end="")
#     print("**")

# 1362 숫자 피라미드

# def fac(n):
#     if n > 1:
#         return fac(n - 1) + n
#     else:
#         return 1


# n = int(input())
# max = fac(n)

# for i in range(n + 1):
#     for j in range(i):
#         print(max, end=" ")
#         max -= 1
#     print()

"""

재귀함수를 활용해 푸는 문제였다.
팩토리얼 활용!
처음에는 팩토리얼인지 몰라 헤맸지만 
팩토리얼이라는 것을 알고 나서 술술 풀렸다. 

"""

# 1380 두 주사위의 합

# k = int(input())
# cnt = 1

# while k - cnt > 0:
#     print(cnt, k - cnt)
#     cnt += 1

"""

cnt의 연산을 while문 안에 안넣어서 엄청난 오류 발생.. ㅋㅋㅋㅋ
바로 수정햇다 ㅠ.ㅠ

"""

# 1405 숫자 로테이션

n = list(map(int, input().split()))

for i in range(n):
    print(*n)
    n.append(n.pop(0))
