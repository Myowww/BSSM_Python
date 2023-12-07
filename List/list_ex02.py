# 2차원 리스트 예제

# 바둑판에 올려 놓을 흰 돌의 개수 n개가 첫 줄에 입력됨
# 둘째 줄부터 n+1번째 줄까지 흰 돌을 놓을 좌표(x, y)가 n줄 입력됨
# n은 10 이하의 자연수이고, x와 y좌표는 1~19까지이며, 똑같은 좌표는 입력되지 않음.

n = int(input())
a = []

for i in range(20):
    a.append([0] * 20)

for i in range(n):
    x, y = map(int, input().split())
    a[x - 1][y - 1] = 1

for i in range(20):
    for j in range(20):
        print(a[i][j], end=" ")
    print()


# 숏코딩_배재현 코드

# 리스트 컴프리헨션(리스트 안에서 반복문 쓰는거)
board = [[0 for i in range(19)] for i in range(19)]

for i in range(int(input())):
    y, x = map(int, input().split())
    # 입력 받은 값 -1 의 값을 0에서 1로 바꾸기
    board[y - 1][x - 1] = 1

for i in range(19):
    print(*board[i])
    # *쓰면 리스트 안에 요소만 공백으로 나눠서 다 출력 가능함
