# a_list = [1, 2, 3, 4, 5]
# print(a_list[:2])
# # a_list 를 첫번째 인덱스부터 2번째 인덱스까지 출력

# print(a_list[2:])
# # a_list 를 2번째 인덱스부터 끝까지 출력

# c_list = [1, 3, 3.14, "hello", [1, 2, 3]]
# print(c_list)
# print(c_list[1:3])  # c_list를 인덱스 1부터 3까지 출력

# d_list = [1, 2, 3, 4, 5]
# print(d_list)
# d_list = 0
# print(d_list)
# # => 리스트의 값은 바뀔 수 있다

# 리스트 예제
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

list = []
for i in range(24):
    list.append(0)

for i in range(n):
    list[a[i]] += 1

for i in range(1, 24):
    print(list[i], end=" ")
