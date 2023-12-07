# 평가 입력받아 다르게 출력하기

score = input()

if score == "A":
    print("best!!!")
elif score == "B":
    print("good!!")
elif score == "C":
    print("run!")
elif score == "D":
    print("slowly~")
else:
    print("what?")


# if 사용하지 않고 풀기
grades = {"A": "best!!!", "B": "good!!", "C": "run!", "D": "slowly~"}

result = grades.get(score, "what?")
print(result)
