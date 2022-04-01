#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://www.youtube.com/watch?v=MYAEv3JoenI
# 함수의 기능을 확장해주는 것이 decorator
# 예를 들어, 나누기 함수를 만들었다면 0으로 나누지 않는지 확인하는 기능을 추가할 수 있다.
# 이런 식으로 추가적인 기능을 덧붙여 주는 것이 decorator 이다.

def check(func):
    def inside(a, b): # Python에서는 함수를 중첩해줄 수 있다
        if b == 0:
            print("Can't divide by 0")
            return
        func(a, b) # 내부 함수에서 이 부분을 놓치지 말고 써줘야 함!
    return inside

@check # 이렇게 @로 표현해주는게 데코레이터
# div = check(div) 원래는 이런식으로 써주는거였음.

def div(a, b):
    return a / b

print(div(10, 0)) # 0으로 나눌 수 없으니까 에러가 발생함

