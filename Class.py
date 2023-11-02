"""

클래스 : 비슷한 작업을 반복하기도 편리하고, 관련된 정보를 한 곳에 모아서 관리하기 위한 틀

객체 : 클래스를 이용해 만들어진 실체
메소드(Method) : 클래스 내부의 멤버로서, 함수의 역할을 수행하는 것. 클래스 내부에서 특정 기능 수행을 담당.

class 클래스명:
    # 생성자
    def __init__(self, ... ):
        속성 정의

    __init__ : 인스턴스를 만들 때 실행되는 초기화 함수 = 생성자
               객체가 처음 만들어지는 순간 딱 한번만 호출되며, 객체의 초기값을 설정하는 역할
    

"""


class Bssm:
    def __init__(self, task, age, name):
        self.team = "부소마"  # Bssm 클래스로 찍어낸 객체들은 모두 team 변수에 부소마가 들어가도록 함
        self.task = task
        self.age = age
        self.name = name

    def intro(self):
        print(
            "안녕하세요 %s에서 %s을 담당하고 있는 %d살 %s입니다."
            % (self.team, self.task, self.age, self.name)
        )


예진 = Bssm("못생김", 28, "김예진")
예진.intro()


# 실습문제
# Grade 클래스 생성, 클래스 안에 메소드를 정의해 다음 코드의 실행결과가 아래와 같이 나오게 하시오

"""

a1 = Grade("나영", 89)
a1.s_grade()

print(a1)

"""


class Grade:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def s_grade(self):
        if self.score >= 90:
            self.grade = "A"
        if self.score >= 80:
            self.grade = "B"
        else:
            self.grade = "C"

    def __str__(self):
        return "%s : %c 등급" % (self.name, self.grade)


a1 = Grade("나영", 89)
a1.s_grade()

print(a1)
