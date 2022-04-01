#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://www.youtube.com/watch?v=fvtk1CwMLh4
# argparse는 사용자가 파이썬 스트립트를 실행할 때, 파이썬 스크립트에게 값(변수)을 전달하고 싶은 상황에 사용한다.

# 인자 설정
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--src', '-s', help="ip src address", required=True)

#변수 선언
args = parser.parse_args()

# parse_args() 함수는 사용자가 입력한 인자를 처리하겠다는 의미의 함수

print(args.src)

# 잘 모르겠따..

