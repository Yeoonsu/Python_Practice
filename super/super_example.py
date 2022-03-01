
#super 썼을때
#상속할 때 child1.__init__(self), child2.__init__(self) 같은 생성자를 
#super().__init__() 한 줄로 줄일 수 있음

class super_Base:
    def __init__(self):
        print('Base.__init__')
        
class super_Child1(super_Base):
    def __init__(self):
        super().__init__()
        print('super_Child1.__init__')
        
class super_Child2(super_Base):
    def __init__(self):
        super().__init__()
        print('super_Child2.__init__')

class super_Child3(super_Child1, super_Child2):
    def __init__(self):
        super().__init__()
        print('super_Child3.__init__')
        
c3 = super_Child3()

# 또 다른 예제
class Ten:
    def adder(self, *args):
        print(sum(args) + 10)
        super().adder()

class Hundred:
    def adder(self, *args):
        print(sum(args) + 100)
        
class Experiment(Ten, Hundred):
    pass

e = Experiment()
e.adder(1, 2, 3)

# 또 또 다른 예제
# https://harry24k.github.io/super/

class A(object):
    def __init__(self):
        print("A")
    
    def hello(self):
        print("hello")
        
class B(A):
    def __init__(self):
        print("B")
    def hi(self):
        print("hi")

# B는 A를 상속받는다      
b = B()
# 출력 : B
b.hello()
# 출력 : hello, A에 있는 hello 함수를 B로 호출했지만 에러 안남

class B(A):
    def __init__(self):
        super().__init__()
        print("B")
    
    def hi(self):
        print("hi")
        
b = B()
# 출력 A (줄바꿈) B (A의 init 함수가 호출됨)

