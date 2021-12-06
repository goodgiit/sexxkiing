# Chapter 04-02
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#        <Loop body>

for v1 in range(10):
    print("v1 is : ",v1)

print()

 # range(10)은 0부터 9까지 만드는 기능을 하고 있다. 여기서 N-1★이라는 점, 콜론(:)을 유의하자. 혹시 range(1000)이라면 0부터 999까지 만들게 된다.

for v2 in range(1, 11):
    print("v2 is : ", v2)

print()

# range(1, 11)는 1부터 11(-1★)=10까지 만드는 기능을 한다,

for v3 in range(1, 11, 2):
    print("v3 is : ", v3)

# range(1, 11, 2)는 1부터 11(-1★)=10까지 2라는 간격차이를 두도록 하는 기능을 한다. 따라서 (1, (2), 3, (4), 5, (6), 7, (8), 9, (10)) 만약 짝수가 나오게 하고 싶음 어떻게 할까? 그 땐 range(0, 11, 2)를 이용하도록 하자.

# collection형태(어떤 집합의 모음)로 빠르게 나타낼 수 있는 반복문

# 1부터 100까지의 합

sum1=0
sum2=0  # 웬만하면 선언은 한꺼번에 하는것이 좋다.


for v in range(1, 1001):
    sum1+=v  # = sum1 = sum1+v(=1~1000)

print('1~1000 Sum : ', sum1)

# range(1, 1001)을통해 1부터 1000까지 만들고 sum1+=v를 이용해 1부터 1000까지 더하면서 반복해나간다. 여기서 진행과정을 살펴보면 처음엔 sum1(=0)+v(1)=1(sum1에 저장) 그 다음 과정 sum1=(=1)+v(=2)=sum1(=3) 그 다음 과정 sum1(=3)+v(=3)=sum1(=6, 0+1+2+3) 그 다음 과정 sum1(=6)+v(=4)=sum1(=10, 0+1+2+3+4) 계속해서 1000(v)을 마지막으로 더하고 print문으로 출력

print('1~1000 Sum : ', sum(range(1, 1001)))

print(range(1, 11))
print(type(range(1, 11)))

# 이 방식을 통해서도 1부터 1000까지의 합을 구할 수 있다. range 함수는 generator iterator라는 것이 나오는데 이것들이 연속적인 데이터를 담고 있는 리스트를 생성해준다. 이를 파라미터 안에 있는 수의 합을 더해주는 기능을 하는 sum함수를 통해 구할 수 있는 것이다.

print('1~1000 사이의 4의 배수의 합 : ', sum(range(4, 1001, 4)))

# sum 함수를 이요해 4의 배수의 합 또한 구할 수 있다. 여기서 간격이 4(3 X)라는 사실에 유의하자. 또한 4의 배수부터 시작이므로 시작점이 1이 아닌 4가 되어야 한다는 점 또한 알아두어야 한다.


for v in range(4, 1001, 4):
    sum2+=v

print('1~1000 사이의 4의 배수의 합 : ', sum2)

# 또한 이 방식을 통해서도 구할 수 있다. 여기서 sum2+=v 행에 print(v)를 넣으면 제대로 4의 배수를 구했는지 알 수 있다. print문을 통해 점검이 가능


# Iterables (반복할 수 있는 객체) 자료형 반복
# 문자열, 리스트, 투플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1 (리스트형) 시퀀스형은 반복문이 가능

names=['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:  # n은 임의대로 해도 무관
    print('Yoo are : ', n)
    # 예제2 (정수형 값)

lotto_numbers=[11, 19, 21, 28, 36, 37]

for L in lotto_numbers:
    print("Current number : ", L)

# 예제3 (문자형)

word="Beautiful"

for s in word:
    print('word : ', s)

# 예제4 (딕셔너리형)

my_info={

    "name": 'Lee',

    "Age": 33,

    "City": "Seoul"

}

for k in my_info:
    print('key :  ', k)

# 딕셔너리형을 반복문에서 이용하면 밸류 값이 없는 키만을 가져온다. 밸류값만을 가져오려면 print('key : ', my_info[k]) 즉 밸류 값을 가져오는 메소드를 이용해야한다. (딕셔너리형의 선언명)[해당키] 또는 get메소드를 이용한  print('key : ', my_info.get[k])로 구성하여도 된다,
# 딕셔너리형을 선언할 때 꼭 다음 키로 넘어가면 콤마(,)를 찍는 것에 유의하자.

for v in my_info.values():
    print('value : ', v)

# 밸류 값만을 가져오는 .values 메소드를 이용하는 것이 가독성이 좋다. 혹은 .items를 이용해 키와 밸류 값 모두를 가져올 수 있다.

# 예제5

name='FineAppLe'

# 대문자는 그대로 소문자는 대문자로 바꾸고 싶어,,

for n in name:  # 이는 name의 문자열 'FineAppLe'을 한글자 씩 반복해나간다.
    if n.isupper():   # isupper은 대문자인지 검사 islower은 소문자인지 검사
        print(n)   # 대문자가 맞다면 그대로 출력
    else:     # 그렇지 않다면(=소문자라면)
        print(n.upper())   # 대문자로 출력

# 한글자씩 개행되서 나오지만 한 문자열로 나오게 할 수 있다. 변수 선언과 더하기 연산으로?


# break문

# 만약 1000명의 학생 중에서 성적이 100점인 친구 1명만을 찾을 때(순차검색) 1부터 처음부터 조회할것이냐? 불필요하게 반복되는 것을 줄이기 위해 반복문을 탈출힐 break문이 존재한다.

numbers=[14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# 숫자 34가 있는 지 없는 지 체크할 때 34만 찾으면 뒤에는 찾을 필요 없이 탈출하게 하는 break문 불필요한 작동이 많으면 실행 시간이 오래 걸릴 수 있다.

for n in numbers:
    if n==34:
        print('Found : 34! ')
        break
    else:
        print('Not Found: ', n)

# break행이 없다면 부득이하게 34 뒤 36, 38이 실행되는 모습을 볼 수있다.
# 반복의 흐름을 제어할 때 필수적으로 사용 if문에서 많이 사용


# continue

# 어떠한 조건 안에서 continue를 만나면 다시 조건을 검사하는 부분으로 이동

lt=["1", 2, 5, True, 4.3, complex(4)] # 문자형, 정수형X2,불린형, 실수형, 복소수형에서 불린형은 출력하고 싶지 않을 때 어떻게 할까?

for v in lt:    # lt안의 원소들 하나씩 반복
    if type(v) is bool:  # 자료형 대조를 위한 "is", "is not" 하나의 원소가 boolen형이냐
        continue  # boolen형이라면 스킵을 시키고(하위구문 진행X) 반복문 행으로 다시 가서 4.3원소로 넘어간다. boolen형이 아니라면 하위구문 그대로 진행
    print("current type : ", v, type(v))
    print("multiply by 2 : ", v*3)

# continue문을 통해 많은 데이터 중에 보기 싫거나 불필요하게 출력되거나 계산되지 않아야 할 값들(ex 위행에선 boolen형의 3배수)이 있을 때 스킵시킬 수 있다.
# continue문 또한 조건 문 하에 들여쓰기를 해야 하는 것에 유의하자.

# for - else

for num in numbers:
    if num ==24:
        print("Found : 24")
        break
    else:
        print('Not Found : 24')


# else문은 실행되지 않았다.(24라는 원소가 numbers변수 안에 있었으므로 for반복문에서 걸림) num == 24가 아닌 49였다면 else문이 실행되어 else문의 하위구문(print('Not Found : 24'))이 실행된다.  즉 for - else문은 for문에서 반복하는 모든 원소를 전부 반복했을 경우에( break문 X) 마지막으로 실행되는 기능을 한다.
# 이를 응용해 끝까지 찾았지만 못 찾은 원소를 구하거나.. 그럴 때 실행됨 파이썬에만 있는 문법이라 볼 수 있다.

# 구구단 출력

for i in range(2, 9): # 2부터 9(-1★)=8까지 만듦
    for j in range(1, 10): # 위행의 하나의 숫자마다(2~8) 1부터 10(-1★)=9까지 만듦 실행횟수는 n의 제곱 즉 9의 제곱 81번
        print('{:4d}'.format(i*j), end='') # chapter01 '{:4d}' 4자리의 문자열 출력(공백을 오른쪽으로 헤) end옵션을 통해 print문으로 인한 자동 줄 바꿈 방지 .format()은 대응방식 chapter02-02에 있다.
    print()

# 변환 예제

name2='Aceman'  # 같은 이름의 변수를 쓰는 것은 좋지 않다.

print('Reversed', reversed(name2)) # 여기까지하고 출력하면  reversed(name2)의 object와 id주소값들이 나오는데 이를 형변환을 통해 올바른 값을 출력해내도록 해야한다,

print('List', list(reversed(name2)))

print('Tuple', tuple(reversed(name2)))

# tuple로 바꿔주기만하면 자료형을 손쉽게 바꿔줄 수 있다.

print('Set', set(reversed(name2)))

# set(집합)은 순서가 없다는 점을 유의하자!(실행시킬 때마다 집합의 원소순서가 달라진다.) 또한 중복되는 문자가 있었다면 하나만 나왔을 것이라는 점을 유의하자,
