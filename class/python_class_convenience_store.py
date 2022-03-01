class Convenience:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price
        
    def info(self):
        print("품목 :", self.category, "/ 이름 :", self.name, "/ 가격 :", self.price)

cracker = Convenience("과자", "크래커", "500")
cracker.info()

class Discount(Convenience):
    def __init__(self, category, name, price, discount):
        self.category = category
        self.name = name
        self.price = price
        self.discount = discount
        
    def discounted(self):
        print(self.name, "은(는)", self.discount, "만큼 할인받는다.")
        
gunbbang = Convenience("과자", "건빵", "300")
gunbbang.info()

hwanta = Discount("음료", "환타", "700", "100")
hwanta.discounted()