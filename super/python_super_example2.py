class happy():
    def __init__(self):
        print("A__init__")
    
    def hello(self):
        print("hello")
        
class sad(happy):
    def __init__(self):
        super().__init__()
        print("B__init__")
    def hi(self):
        super().hello()
        print("hi")
        
unit = sad()
super(sad, unit).hello()

# super(하위클래스의 이름, 하위클래스의 객체(object)).상위클래스의 함수()