class FishBreadMaker:
    def __init__(self, **kwargs):
        self.size = 10
        self.flavor = "팥"
        self.price = 100

        if "size" in kwargs:
            self.size = kwargs.get("size")
            # kwargs 딕셔너리 안에 size라는 key값이 있나? 있으면 가져와서 size 변수에 대입
        if "flavor" in kwargs:
            self.flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self.price = kwargs.get("price")

    def show(self):
        print("붕어빵 크기 : {}".format(self.size))
        print("붕어빵 종류 : {}".format(self.flavor))
        print("붕어빵 가격 : {}".format(self.price))
        print("*" * 30)


fish1 = FishBreadMaker()
fish2 = FishBreadMaker(size=20, price=300)
fish3 = FishBreadMaker(flavor="초콜릿", size=15)

fish1.show()
fish2.show()
fish3.show()

# 붕어빵기계 클래스를 상속받은 마켓굿즈


class MarketGoods(FishBreadMaker):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self.market_price = self.price + margin

    def show(self):
        print(self.flavor, self.market_price)


fish1 = MarketGoods
fish1.show()
