# 다양한 출력구문
print("나는 %s을 좋아해요" % "파이썬")
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))
# 인덱스 넘버로 넘버링 가능!

age = 20
color = "RED"
print(f"나는 {age}살이며, {color}을 좋아해요")


###


def profile(name, age=17, lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주사용언어: {2}".format(name, age, lang))


profile("이나영", 17, "C")

# 함수의 키워드 값
# 매개변수의 값을 키워드 = 값 형태로 전달하면 매개변수의 순서가 뒤바뀌어도 해당 변수로 찾아감.
profile(age=16, name="이나영", lang="C")


###


# 가변인자함수
def func(*a):
    return max(a)


print(func(1, 2, 3, 4, 5))
print(func(3, 6, 9))


###

"""

listname.pop()                  : 리스트 맨 뒤에 있는 값을 삭제 + 반환
listname.pop(index)             : 해당 인덱스에 위치한 값을 삭제 + 반환
listname.append()               : 리스트 맨 끝에 항목 추가
listname.insert(index, value)   : 해당 인덱스에 값 추가
del listname[index]             : 인덱스 이용해서 삭제
    a1 = list(map(int, input().split))
    print (*a1)

"""
