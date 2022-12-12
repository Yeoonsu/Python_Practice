class Cal:

    #생성자 : 메모리에 올라오는 순간 즉시 실행됩니다.
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a/self.b

cal1 = Cal(1, 2)
# cal1은 self가 가르키게 됨

# 1은 a가 가르키게 됨
# 2는 b가 가르키게 됨

print(cal1.a)
print(cal1.b)
print(cal1.add())