# 19x19 판 초기화
board = [list(map(int, input().split())) for i in range(19)]

for i in range(int(input())):
    y, x = map(int, input().split())
    for j in range(19):
        board[j][x - 1] = int(not board[j][x - 1])
        board[y - 1][j] = int(not board[y - 1][j])

[print(*i) for i in board]
