n = int(input())

score = list(map(int, input().split()))
grade = sorted(score, reverse=True)

for i in range(n):
    print(score[i], end=" ")
    index = grade.index(score[i]) + 1
    print(index)
