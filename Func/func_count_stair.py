"""

함수 예제

입력)
첫째 줄에 계단의 개수가 주어진다. 
둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
계단의 개수는 300이하의 자연수이고, 
계단에 쓰여 있는 점수는 10000이하의 자연수이다.

출력) 
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최대값을 출력한다.

알고리즘
1. 첫 번째 계단
list[0] = st[0]

2. 두 번째 계단
list[1] = st[0] + st[1]

3. 세 번째 계단
list[2] = st[1] + st[2] || st[0] + st[1]

"""

"""# 계단의 개수
n = int(input())

# 계단에 쓰여있는 점수
score = [int(input()) for i in range(n)]

# dp 리스트
dp = [0] * (n)

# 총 점수의 최대값 출력
# 계단이 2개 이하(3개 미만)일 때에는 다 더하기
if n < 3:
    print(sum(score))
# 계단이 3개 이상일 때
else:
    # 첫째 계단 수동 계산
    dp[0] = score[0]

    # 둘째 계단까지 수동 계산
    dp[1] = score[0] + score[1]

    # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])
    print(dp[-1])
"""

# 전유진 코드

n = int(input())  # 계단 개수 입력받기
s = [int(input()) for _ in range(n)]  # 계단 점수 받기


# 점수 세는 재귀함수
def f(i, cnt):
    if i >= n:
        return 0
    if cnt == 2:
        return f(i + 1, 0)
    # i가 1 또는 2가 아니면
    else:
        return max(f(i + 1, cnt + 1) + s[i], f(i + 1, 0))


print(f(0, 0))
