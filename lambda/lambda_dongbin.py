# https://www.youtube.com/watch?v=11GTb0SsQHI
# 람다식을 이용하여 함수의 정의 과정을 짧고 간편하게 만들 수 있음

# 람다식 : 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법
add = lambda x, y: x + y
print(add(1, 2))

# map() : 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와줌.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

my_function = lambda a, b: a + b
result = map(my_function, list1, list2)
print(list(result))
#map을 사용하여 list1과 list2의 각 원소에 대해서 하나씩 적용 가능함

# https://www.youtube.com/watch?v=BcbVe1r2CYc
def func(x) : 
    return x+5

func2 = lambda x: x+5

print(func2(9))
print(func(2))


def func3(x):
    func2 = lambda x: x+5
    return func2(x) + 85

print(func3(2))

func33 = lambda x,y : x+y
print(func33(5,5), func33)

func333 = lambda x,y=4 : x+y
print(func333(5), func333)


a = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(func,a))
newList2 = list(filter(lambda x: x%2==0, a))
print(newList2)



