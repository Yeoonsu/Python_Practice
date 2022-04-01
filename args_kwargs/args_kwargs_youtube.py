# https://www.youtube.com/watch?v=c2AN1-6-NXk

# 두가지만 기억하기 ! 
# args : tuple
# kwargs : dict

# 줄 때는 풀고, 받을 때는 묶는다 ( *는 tuple로, **는 dict로 )

def sum(a, b):
    return a + b

sum(1, 3)
# 결과값 3 return

t = (2, 3)
sum(t)
# error

sum(*t)
# 정상적으로 결과값 5 return


# 매개변수를 정의할 때, 매개변수에 별(*)이나 별별(**)을 사용하게 되면 전달받은 매개변수들을 하나로 묶어주겠다는 의미임.
# 별(*) 사용해보기
def sum2(*args):
    result = 0
    for i in args:
        result += i
    return result

sum2(1, 2, 3)
# return 6
# tuple (1,2,3) 은 args 변수에 할당이 된다


# 별별(**) 사용해보기
def sum(a, b): 
    return a+b

d = {'a':3, 'b':4} # 딕셔너리로 전달 가능
sum(**d)

# return 7

def person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
        
person(name='PythonTube', age=38, weight=70)

# return
# name PythonTube
# age 38
# weight 70

p = {'name':'PythonTube', 'age'=20, 'weight':50}
person(p)
#error

person(**p)
# return
# name PythonTube
# age 20
# weight 50