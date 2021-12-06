# Chapter04-1

# 파이썬 제어문

# IF 실습



# 기본 형식

print(type(True))

# True : 0 이 아닌 수, "abc", [1, 2, 3..](데이터가 있는 리스트), (1, 2, 3...) (데이터가 있는 튜플), {1, 2, 3...} (데이터가 있는 딕셔너리), 데이터가 있는 집합 등.

print(type(False)) # False : 0, "", [], (), {}... (0, 빈 문자열, 리스트, 튜플, 딕셔너리,집합)

# True는 1 False는 0

# 예1

if True:
     print('Good')

  # if는 True면 하위구문이 진행되고 False면 진행되지 않는다. 또한 True를 지칭하는 0이 아닌 수 어떤 문자열 등이 오게 되면 진행되지만 False를 지칭하는 0, 빈 문자열 등ㅇ 오면 하위구문이 진행되지 않는다.

# if 다음에 조건식 if는 들여쓰기 (indent)를 진행해야 한다. 하지 않으면 에러가 발생한다.

if False:
    print('Bad')

# 예2

if False:
    print('Bad! ')

else:
    print('Good! ')

print()

# else 는 위에 조건문을 부정하는 기능을 한다. if False이므로 else는 True로 하위구문이 실행이 된다.

# 관계 연산자

# >, >= , <, <=, ==, !=

x=15
y=10

# 양 변이 같은 경우 참

print(x==y)

# == 관계 연산자는 두 변수가 같은가?를 묻는 연산자이다. 위에서는 x=15이고 y=10이므로 같지 않아서 False가 출력된다.

# 양 변이 다를 때 참

print(x!=y)

# != 관계 연산자는 두 변수가 다른가?를 묻는 연산자이다. 위에서는 x=15이고 y=10이므로 다르기 때문에 True가 출력된다.

# 좌변이 클 때 참 (15>10 이므로 참)

print(x>y)

# 죄변이 크거나 같을 때 참 (15>=10 이므로 참)

print(x>=y)

# 우변이 클 때 참 (15<10은 거짓)

print(x<y)

# 우변이 크거나 같을 때 참 (15<=10은 거짓)

print(x<=y)

city=""

if city:
    print("You are in:", city)

else:
    print("Please enter your city")

# city라는 변수가 빈 문자열이므로 if다음의 조건문에서 False이므로 하위구문이 실행되지 않고 else문에서 실행된다. 하지만 city 변수를 "Seoul"로 선언하면 if 조건문이 True라서 if의 하위구문이 실행되어 "You are in Seoul"이 출력된다.

city2="Seoul"
if city2:
    print("You are in:", city2)
else:
    print("Please enter your city")
    # 논리 연산자(중요)

# and, or, not

a=75

b=40

c=10

print('and: ', a>b and b>c) # a>b>c

# and 연산자는 조건을 모두 만족해야 True(참)를 출력한다. 위에서는 (75>40) a가 b보다 크고 (40>10) b가 c보다 크므로 True를 출력한다. 하지만 c=50이라면 a>b를 만족하지만 b>c를 만족하지 못하므로 False값을 출력한다.

print('or : ', a>b or b>c)

# or 연산자는 두 조건 중 하나만 만족해도 True(참)를 출력한다. 위에서는 (75>40)a가 b보다 크므로 이미 하나를 만족했으므로 True가 출력된다. 여기서는 c=50이어도 True가 출력된다. 앞부분(a>b)이 True면 뒷부분(b>c)은 실행되지도 않는다.

print('not', not a>b)

# not 연산자는 반대로 출력해주는 기능을 가진 연산자이다. a>b = 75>40이므로 True이다. 앞에 not가 있으므로 not True = False가 출력된다.

print(not True)

print(not False)

print()

# 산술, 관계, 논리  우선순위 (산술 > 관계 > 논리)

print('e1: ', 3+12>7+3)

print('e2 : ', 5+10*3>7+3*20)

# 모두 먼저 계산(산술)한뒤 크고작음(관계)순으로 판단된다.

print('e3 : ', 5+10>3 and 7+3==10)

# 산술(5+10=15, 7+3=10)먼저 진행 후 관계(10>3=True, 10==10 => True)진행 후 논리(True and True => True)순으로 진행되어 True를 출력한다.

print('e4 : ', 5+10>0 and not 7+3==10)

# 산술(5+10=15, 7+3=10) 후 관계(15>0 =>True, 10==10 =>True)후 논리(True and not True(=False) )=> False순으로 진행되어 False값이 출력된다.

score1=90

score2='A'

# 복수의 조건이 모두 참일 경우에 실행 and 연산자

# 예4

if score1>=90 and score2== 'A':
    print('Pass')

else:
    print('Fail')

# score1=90이고 score2='A'이므로 True and True 즉 True이므로 if의 조건문을 만족하므로 if의 하위구문이 실행되어 Pass 값을 출력한다. else의 하위구문은 실행되지 않는다.여기서 score1=70점이라면 if의 조건문을 만족하지 못하므로(False and True => False)이므로 else의 하위구문이 실행된다.

# 들여쓰기는 4번 띄어쓰기

# 예5

id1='vip'
id2='admin'
grade='platinum'

if id1=='vip' or id2=='admin':
    print('관리자 입장')

# vip 또는 admin이면 관리자

if id2=='admin' and grade=='platinum':
    print('최상위 관리자')

# admin 중 platinum이어야 최상위 관리자.
# 예 6

# 다중조건문

num=90

if num>=90:
    print('Grade : A')
elif num>=80:
    print('Grade : B')
elif num>=70:
    print('Grade : C')
else:
     print('과락')

print()

# elif를 이용해 조건문을 계속해서 붙일 수 있다.

# 예7

# 중첩 조건문

grade = 'A'
total=95

if grade =='A':
    if total>=90:
        print('장학금 100%')
    elif total>=80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

# if문의 하위구문에 if, elif문을 이용해 중첨 조건문을 구성할 수 있다. 하지만 너무 많은 if문을 중첩시키는 것은 가독성이 떨어지기 때문에 좋지 않다.
# if문에서도 역시 괄호의 짝과 조건에 맞는 들여쓰기를 잘해야 한다.


# in, not in

q=[10, 20, 30]   # 리스트형

w={70, 80, 90, 100}  # 집합형

e={"name" : "Lee", "city" : "Seoul", "grade" : "A"} # 딕셔너리형

r=(10, 12, 14)

print(15 in q)

print(90 in w)

print(12 not in r)

print("name" in e)

print("Seoul" in e.values())

# 여기서 e는 딕셔너리형이다 그 원소 중 "Seoul"은 밸류 값이기 때문에 그냥  print("Seoul" in e.)을 하게되면 False값이 나온다. 여기서 밸류 값을 가져오는 기능을 가진 vaues를 이용해야 한다.
