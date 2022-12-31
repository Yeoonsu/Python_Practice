# chapter03-01
# special method(magic method)
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(functions), class(클래스)

# 매직 메소드 : 클래스 안에 정의할 수 있는 특별한(이미 만들어진, built-in) 메소드. __init__ 이런 것들

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n*100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def __str__(self):
        return 'Fruit Class Info : {}. {}'.format(self.name, self._price)

    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._price >= x._price:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._price <= x._price:
            return True
        else:
            return False
    
    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._price - x._price

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직메소드 출력
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)