# 모듈 사용 실습

import sys

print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
#sys.path.append('C:/math')
#영구적으로 등록하는 것은 구글 검색
#완전히 검증되기 전에는 경로 삽입을 가급적 하지 않는게 좋음

print(sys.path)

#import test_module

# 모듈 사용
# print(test_module.power(10, 3))

import basic_module

print(basic_module.add(10, 100000))


