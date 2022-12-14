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
cal2 = Cal(3, 4)

# cal1은 self가 가르키게 됨

# 1은 a가 가르키게 됨
# 2는 b가 가르키게 됨

# print(cal1.a)
# print(cal1.b)
# print(cal1.add())

# print(cal2.a)
# print(cal2.b)

# 클래스가 익숙해지면 오히려 더 쉽고 편안하다

cal1.a = 7 # namespace 변경

print(cal1.a)
print(cal1.b)
print(cal1.add())
