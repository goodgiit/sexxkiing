# 연관 관계가 있는 변수, 함수, 클래스 이런 것들을 모아놓은 파일을 모듈이라 한다.

# 다른 파일에서 내가 필요할 때 가져와서 사용할 수 있다. (=재사용이 가능하다.) ex) import math -> math.pi 파이썬 내부적으로 가져다 쓰는 모듈

# ex) import random -> random.random 에서 실행하면 'built-in method' 가 출력되는데 이는 이미 파이썬 내부적으로 만들어져 있는 것이다. 이를 random.random()으로 호출하면 0부터 1 사이의 난수가 생성된다. 이도 모듈과 같다.

# 우리가 만든 것을 모듈로 등록해서 가져다 써보는 실습을 해보자

# Chapter06-2

# 파이썬 모듈 : 다른 프로그래밍에서도 비슷한 기능을 내는 모듈 (모듈화를 해서 만들다 : 재사용이 가능, 공용으로 사용 가능, 해당 기능에 딱 맞게{여러 기능이 결합된 거이 아닌 그래야 재사용이 쉬우니까} 만든다는 의미)

# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

# 사직연산을 하는 모듈을 등록해보자

def add(x, y):

    return x+y

def subtract(x, y):

    return x-y

def multiply(x, y):

    return x*y

def divide(x, y):

    return x/y

def power(x, y):

    return x**y

# x**y는 x에 y제곱을 의미한다. 이 대신 power함수를 사용해도 좋다.

# print('-'*15) # 구분선
#
# print('called! inner!') # 내부에서 선언되었다는 의미의 문자열
#
# print(add(5, 5))
#
# print(subtract(15, 5))
#
# print(multiply(5, 5))
#
# print(divide(10, 2))
#
# print(power(5, 3))
#
# print('-'*15)

# 올바르게 함수가 기능을 하는 지 확인하기위한 print문

# 함수 바로 밑에서 출력되었으므로 내부에서 출력된 것이다.

# 만약에 다른 파일을 만들고 사칙연산이 필요하다면 다시 이렇게 4개의 함수들을 선언할 것인가? 코드 중복으로 인해 효율성이 떨어진다.

# 그 때 이것을 모듈로 등록해서 다른 파일에서 가져다 쓸 수 있다면 (재사용할 수 있다면) 효율성이 증대될 것이다.

# 모듈화된 것을 재사용하는 과정을 보여주기 위해  moudle_test.py파일 생성





# 모듈 사용 실습

import sys

import time

print(time.time())

# sys랑 time은 파이썬이 위치를 알고 있기 때문에 이렇게 가져다 쓸 수 (import) 있는 것이다.

print(sys.path)

# 파이썬 안의 모듈들, 패키지들은 어디에 등록이 되있는데 이에 대한 경로를 추적하는 기능을 하는 sys.path

# sys.path 경로 안에서 내가 만들어놓은 모듈 또는 그 모듈들을 모아놓은 패키지를 검색할 수 있다.

print(sys)

# 위 행을 통해 built-in : 이미 파이썬 내부적으로 사용하는 것이기 때문에 만들어진 것이다(모듈). 즉 sys도 sys.path 경로  안에 존재한다.

# 즉 sys.path 경로 안에 있다면 어디서든지 import로 모듈을 가져올 수 있다. 여기서는 chapter06_02.py를 다른 곳(python_basic 상위 폴더에서 임의의 폴더 python_moudle을 만듦)으로 옮겨놓고 등록 해보는과정을 밟아보자.

# 모듈들을 모아놓은 것을 패키지라 한다.

# 나한테 쓸모없는 print문을 제거하기 위한 main 예약어의 기능을 알아보자.

# __name__ 사용

if __name__ == "__main__":

    print('-'*15)

    print('called1 __main__')

    print(add(5, 5))

    print(subtract(15, 5))

    print(multiply(5, 5))

    print(divide(10, 2))

    print(power(5, 3))

    print('-'*15)

# crtl + ? = 한꺼번에 주석처리

# 실행하는 위치가 다른 데서 import해서 chapter06_02.py를 호출할 때 메인 실행하는 파일은 moudle_test.py 파일이다.
