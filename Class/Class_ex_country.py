"""

국가 클래스 만들기
초기화 : 국가명, 인구, 수도

show() 메서드 만들기
-> "국가 클래스 메소드입니다" 출력하기

국가 클래스를 상속받아 대한민국 클래스 만들기

"""


class Country:
    def __init__(self, **kwargs):  # ** 은 가변인자를 의미
        self.name = "대한민국"
        self.people = 100
        self.capital = "서울"

        if "name" in kwargs:
            self.name = kwargs.get("name")
        if "people" in kwargs:
            self.people = kwargs.get("people")
        if "capital" in kwargs:
            self.capital = kwargs.get("capital")

    def show(self):
        print("국가 클래스 메소드입니다")


class Korea(Country):
    def __init__(self, **kwargs):  # ** 은 가변인자를 의미
        super().__init__(**kwargs)

    def show(self):
        print(f"국가명 : {self.name}")
        print(f"국가명 : {self.people}")
        print(f"국가명 : {self.capital}")


c1 = Country()
c1.show()

k1 = Korea()
k1.show()

# 파이썬의 상속은 자바의 상속과 달리 여러 개를 상속받을 수 있다!
