# Chapter03-1
# 숫자형
# 파이썬 지원 자료형

"""

int : 정수
float : 실수
complex : 복소수
bool : 불린 ( true면 참 false면 거짓)
str : 문자열(시퀀스) 시퀀스는 반복 처리 가능 순서가 있다는 의미
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

"""

# 데이터 타입

str1="Python"  # str타입

bool= True # or False

str2='Anaconda'

float_v=10.0     # 10 == 10.0 엄연히 파이썬면에서 다른 숫자이다. 10은 정수형 타입(int)이고 10.0은 실수형 타입(float)

int_v=7

list=[str1,str2] # 시퀀스형의 양식 [,......,.....] []파라미터 안에 데이터 적재(줄서기)가 가능하다.

print(list)

dict={

"name" : "Machine Learning",

"version" : 2.0

}

# dict의 형태로는 앞의 "name"과 "version"을 key라고 한다 각 key의 내용물들은 각각 "Machine Learning" ,  2.0이 된다,

tuple=(7, 8, 9)  # tuple은 소괄호()를 사용한다.

tuple=7, 8, 9  # tuple은 괄호없이 콤마로만 나열해도 실행가능

set={7, 8, 9}  # set는 중괄호{}를 이용한다.

# 괄호에 따라 데이터 타입이 달라질 수 있다,



# 데이터 타입 출력

print(type(str1))

print(type(bool))

print(type(float_v))  # 오류 방지를 위한 _v 삽입

print(type(int_v))

print(type(dict))

print(type(tuple))

print(type(set))

# 숫자형 연산자

"""

+

-

*

/

// : 나눈 다음 몫을 반환

% : 나눈 나음 나머지 반환

abs(x) : 절대값

pow(x, y) : x ** y : x에 y제곱 ex) 2**3=8=pow(2, 3)

"""

# 정수 선언

i=77

i2=-14

big_int=777777777777777777999999999999

# 큰 수도 할당 가능

# 정수 출력

print(i)

print(i2)

print(big_int)

print()

# 실수 출력

f=0.9999

f2=3.141592

f3=-3.9

f4=3 / 9

# 실수 출력

print(f)

print(f2)

print(f3)

print(f4)

print()

# 연산 실습

i1=39

i2=939

big_int1=77777777777777777777779999999999999999

big_int2=3443419885137813478271362173614777777

f1=1.234

f2=3.939

# +

print(">>>>>+")

print("i1+i2 : ",i1+i2)

print("f1+f2 : ", f1+f2)

print("big_int1+ big_int2: ",big_int1+big_int2)

print()

# *

print(">>>>>*")

print("i1*i2 : ",i1*i2)

print("f1*f2 : ", f1*f2)

print("big_int1* big_int2: ",big_int1*big_int2)

print()

# 형 변환 자동화

a=3+1.0   # 정수형 + 실수형

print(a)  # 실수형 숫자 출력

print(type(a))   # 실제로도 실수형 타입이다.
# 형 변환 실습

a=3. # 3. = 3.0 (0생략 가능)

b=6

c=.7  # .7 = 0.7

d=12.7

# 타입 출력

print(type(a), type(b), type(c), type(d))

# 형 변환

print(float(b))

# 원래 b=6(정수형)이었으나 6.0(실수형)으로 형 변환 되었다.

print(int(c))

# 여기서도 c = 0.7(실수형)이었으나 0(정수형)으로 형 변환  즉 .7 절삭

print(int(d))

print(int(True))

print(float(False))

 # 이는 불린형? True : 1 , False : 0을 알아두면 print(int(True))=1 print(float(False))=0.0임을 알수 있다.

print(complex(3))

print(complex('3')) # '3'이라는 문자형을 숫자형으로 내부적으로 자동으로 바꾼 다음 complex에 의해 복소수형으로 변환

print(complex(False))

# 형 변환은 해당 형 변환을 해주는 함수 파라미터 안에 변환해주고자 하는 데이터형을 넣어주면 자동으로 변환

# 수치 연산 함수

print(abs(-7))  # 절댓값으로 변환해주는 함수

x, y = divmod(100, 8)  # x에 100을 8로 나눈 몫과 y에 그 나머지를 할당한다.

print(x, y)

print(pow(5, 3), 5**3)

# 외부 모듈 math를 이용(좀 더 수학적 계산 가능)

import math

print(math.pi) # 원주율 계산

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
