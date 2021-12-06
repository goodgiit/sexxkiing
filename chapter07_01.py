# 예외 : 사용자가 작성한 코드에서 비정상적으로 발생하는 사건  예측 가능한 예외와 예측 불가능한 예외가 있다. 걀국 중간에 잘못된 값을 발생시키거나 의도한 대로 작동하지 않으면 예외라고 볼 수 있다.

# 예측 가능한 예외 : 아이디 비번 틀리는 것들 등 예측 불가능한 예외는 하드디스크 량 부족 등

# 에러는 예외와 다르게 어떤 운영환경에서 발생한다. ex) 정전 급고장 하드웨어적 고장 등등..

# Chapter07-1

# 파이썬 예외 처리의 이해

# 예외 종류

# SyntaxError(문법 오류), TypeError(숫자에 문자를 더한다거나 더할수 없는 두 자료형을 더할 때등등), NameError(없는 변수를 참조할 때), IndexError(예를 들어 index가 3개 즉 0번 1번 2번까지 있는데 3번으로 접근한다거나 등), ValueError, KeyError

# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요(예상하지 못했는데 실행함으로써 발견한 예외) 검증!

# 1. 예외는 반드시 처리 ★

# 2. 로그는 반드시 남긴다.(로그란 어떤 예외가 발생했는지에 대해 기록(증거)을 남긴다.) 많은 프레임워크가 있다.

# 3. 예외는 던져진다.

# 4. 예외 무시(좋은 방법은 아니다.)



# SyntaxError(문법적 오류)

# print('error)  따옴표 쌍이 안 맞는 경우

# print('error'))  괄호 쌍이 안맞는 경우

# if True   # 조건문 등에서 콜론 안붙인 경우

    # pass



# NameError : 참조 없음

# a=10

# v=15

# print(c)

# 거의 오타에 의해 많이 발생한다



# ZeroDivisionError

# print(100/0) 예외의 이름 그대로 0으로 나누려고 할 때 발생하는 예외



# IndexError

# x=[50, 70, 90]

# print(x[4])

# x리스트에는 0번 1번 2번 총 3개의 인덱스가 있으나 print문은 x리스트에 없는 4번 인덱스를 참조하기 때문에 예외 발생 주로 for문에서 나올 수 있는 예외이다.

# print(x.pop())

# print(x.pop())

# print(x.pop())

# pop메소드를 이용해서 x리스트의 마지막 인덱스부터 하나씩 가져와 제거하고 있는데 x리스트의 원소는 3개이나 4번 pop메소드를 이용하면 IndexError가 발생한다.

# KeyError (주로 딕셔너리형에서 발생)

# dic ={'name' : 'Lee', 'Age': 41, 'City' : 'Busan'}

# print(dic['hobby'])

# dic 딕셔너리에는 'hobby' 키가 없으므로 KeyError 발생

# print(dic.get('hobby'))

# 이런 이유로 Get 메소드를 사용하는 것이 안전 (예와가 발생하지 않고 None 출력)



# 예외 없는 것을 가정하고 프로그램을 작성해라 -> 런타임(실행)할 때 예외 발생 시 예외 처리 권장(EAFP)

# AttribuetError : 모듈, 클래스에 있는 잘못된 속성 사용 예외

# import time

# print(time.time2())

# 파이썬이 이미 갖고 있는 모듈 파일 time에는 time2라는 메소드가 존재하지 않으므로 AttributeError가 발생

# ValuError : 참조값 없을 때 발생

x=[10, 50, 90]

x.remove(50)

print(x)

# x.remove(200)

# x 리스트에는 200이 존재하지 않는데 200을 제거하라는 코드 때문에 ValueError가 발생

# 시퀀스형 자료 안에서 어떤 데이터를 참조하려 하는데 발생하지 않을 때 발생한다.



# FileNotFoundError

# f=open('test.txt')

# 위 코드의 기능은 현 위치에서 test.txt 파일을 가져오라는 기능을 하는 코드이나 현 위치('python_basic' 폴더)에는 test.txt 파일이 없기 때문에 FileNotFoundError 발생



# TypeError(가장 많이 발생) : 자료형에 맞지 앟는 연산을 수행할 경우

x=[1, 2]

y=(1, 2)

z='test'

# print(x+y)

# x는 리스트형이므로 가변형(수정/삭제 가능)이지만 y는 튜플형으로 불변형(수정/삭제 불가능)이므로 서로 연산이 불가하므로 TypeError 발생

# print(x+z)

# print(y+z)

# 물론 리스트형과 문자형 연산, 튜플형과 문자형 연산들도 예외가 발생한다.

print(x+list(y))

print(x+list(z))

# 물론 형변환을 통해 연산이 가능하다.



# 예외 처리 ★

# try : 예외가 발생할 가능성이 있는 코드를 try로 실행

# except 에러명1 : 여러개 가능

# except 에러명2 :

# else : try 블록의 에러가 없을 경우 실행 (break문을 만나지 않았을 경우 else문이 실행되는 특징 이용)

# 즉 try문에서 에러가 발생하지 않았을 경우에는 else문이 실행 try문에서 에러가 발생했을 경우 except 들이 실행된다,

# finally : 항상 마지막에 실행

name =['Kim', 'Lee', 'Park']

# 예제 1

# try문 아래에서 예외가 발생할 가능성이 있는( 어떤 파일을 처리한다든지 데이터베이스를 연동한다든지 다른 사이트에 접속해서 크롤링을 해온다든지  - 내가 작성한 코드는 정확해도 외부의 방문한 서버 문제가 있을 수 있고 커넥션에 있어 에러가 발생할 수 있기 때문에) 코드들을 try문에 넣는다.

# try:
#
#     z='Kim'
#
#     x=name.index(z) # z='Kim'이므로 index 0번이 들어간다. index(z)=index(0)
# 
#     print('{} Found it! {} in name'.format(z, x+1))

# z = 'Kim' 이 출력될 것이고 x+1은 인덱스(번호)는 -1(★)을 하므로 몇 번째 원소인지 보여주기 위해서 +1을 한 것이다.

# except ValueError:
#
#     print('Not found it! - Occured ValueError')

# 어떤 예외가 발생할 확률이 높을까 바로 ValueError다. 그 이유는 try문을 통해 외부의 코드를 가져왔는데 여기서 name 리스트에서 'Kim'이 없을 수도 있다는 경우하에 발생할 수 있는 예외는 ValueError이기 때문이다.

# 위 코드의 기능은 try문에서 예외 발생 시 그 예외가 ValueError면 except의 하위구문 print문을 통해 문자열을 출력하는 기능을 하고 있다. 즉, 일종의 조건문인 셈이다.

# else:
#
#     print('Ok! else.')
#
#
#
# print()

# else문의 기능은 try문에서 예외 발생하지 않을 시 하위구문의 print문을 출력하는 기능을 하고 있다.

# 위 try문에서 예외 발생하지 않으므로 else문이 실행된다.

# 만약 z='Cho'로 바꾸게 되면 ValueError가 발생해서 except문에서 ValueError를 처리해주고 이의 하위구문 print문이 실행된다.

# print('pass')

# z='Cho'라는 가정하에 예외를 잡았기 때문에 프로그램이 종료되거나 그러지 않고 계속해서 런타임이 가능하다.

# 예제 2

# try:
#
#     z='Kim'
#
#     x= name.index(z)
#
#     print('{} Found it! {} in name'.format(z, x+1))
#
# except:
#
#     print('Not found it! - Occured ValueError!')

# 예제 1과의 차이점은 except문에서 ValueError를 명시해주지 않았다는 것이다. 이렇게 되면 except문은 모든 에러를 잡게 된다. 단점은 어떤 에러가 발생했는 지를 정확하게 알 수 없다는 것이다. excep문 뒤에 빈 칸으로 두거나  Exception을 명시해 주기도 한다.

# else:
#
#     print('Ok! else!')
#
# print()

# 예제 3

# try:
#
#     z='Cho'
#
#     x= name.index(z)
#
#     print('{} Found it! {} in name'.format(z, x+1))
#
# except Exception as e :

# alias를 이용해 Exception의 별명 e로 설정
    #
    # print(e)

# 설정 후 e를 print문으로 출력하면 예외 내용을 출력할 수 있다.

#     print('Not found it! - Occured ValueError!')
#
# else:
#
#     print('Ok! else.')

# 가장 좋은 것은 예외 종류(여기서는 ValueError)를 명시해 주는 것이 좋다.(로그를 남기는 데도 확실하기 때문에)

# finally:
#
#     print('Ok! finally!')

# 예외가 발생했음에도 finally문은 실행되었다. 이를 통해 finally문은 무조건 한 번 실행된다는 것을 알 수 있다.

print()

# 예제 4

# 예외 고의적 발생 : raise 키워드

# raise 키워드로 예외 직접 발생

try:

    a='Park'

    if a=='Kim': # (어떤 사이트를 운영하는데 관리자 'Kim'이 로그인할 시 )

        print('OK! Pass!')

    else:

        raise ValueError

# 'Kim'이 아닌 다른 것이 접속하려는 상황을 아주 심각한 상황이라 해보자. 여기서 raise 키워드를 통해 예외를 발생시킬 수 있다.

# 실제로 위 코드에선 ValueError가 발생할 조건(index에 값이 없는 등.)은 아니지만 raise 키워드를 통해 고의로 발생

except ValueError:

    print('Occured Exception!')

else:

    print('Ok! else!')

# except문과 else문을 통해 예외가 발생했는 지 알 수  있다.

# 실습할 땐 예제 하나씩 주석 풀면서 실행시키면 된다.

# 많이 사용하는 방식은 예제 3
