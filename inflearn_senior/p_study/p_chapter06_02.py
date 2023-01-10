# Chapter06-02
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# Generator Ex1
def generator_ex1():
    print('Start')
    yield 'A point.'
    print('continue')
    yield 'B point.'
    print('End')

temp = iter(generator_ex1())

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

print()

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

print()
print()

for i in temp3:
    print(i)

print()
print()

# Generator Ex3(중요 함수)
# filterfalse, accumulate, chain, product, groupby
import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1)) # 2.5씩 증가함
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

print()

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print(v)

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print(v)

    # [3, 4, 5]

print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1,11,2))
print(list(gen5))
# ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7))
# [('A',), ('B',), ('C',), ('D',), ('E',)]

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D'), ('D', 'E'), ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'), ('E', 'E')]

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')
#print(list(gen9))

for chr, group in gen9:
    print(chr, ' : ', list(group))

print()
# A  :  ['A', 'A', 'A']
# B  :  ['B', 'B']
# C  :  ['C', 'C', 'C', 'C']
# D  :  ['D', 'D']
# E  :  ['E', 'E', 'E']