# 모듈 만들기 실습

import csv, os
# 새롭게 시작할 때 csv 모듈을 먼저 임포트 합니다
def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output
# opencsv() 함수에서는 f를 파일 객체로 해 직접 open 하는 방식을 사용했습니다

def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)
# writecsv() 함수에서는 with 문을 사용해 코드 길이가 조금 더 짧습니다.
