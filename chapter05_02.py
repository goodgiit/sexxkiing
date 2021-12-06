# Chapter05-2

# 어떤 데이터(영문이든 한글이든 숫자든)를 사용자가 입력 실행,런타임 때 사용자에게 데이터를 받아서 그 데이터를 함수에서 활용할 수도 있고 또 일반적인 파이썬 연산을 이용해서 의도하는 출력값으로 나타내는것 =문제해결 과정(알고리즘) 입력이 있고 알고리즘이 있고 출력이 있고 주제를 정하고 주제를 해결할 때까지의 일련의 단순회되고 컴퓨터가 알아들을 수있도록 하는 것을 프로그래밍이라 한다.

# 파이썬 사용자 입력

# Input 사용법

# 기본 타입(str) (무조건 문자열로만 입력받는다라는 사실!)



# 예제 1

name=input("Enter Your Name : ")

grade=input("Enter Your Grade : ")

company=input("Enter Your Company Name : ")

# 런타임 때 입력을 받겠다는 의미 = input() 괄호 안은 사용자에게 보여질 문구 내용 작성

print(name, grade, company)

# 이 상태로 실행하면 아무 일도 일어 나지 않는다 이유는 현재의 아톰 콘솔에서는 터미널 환경이 아니기 때문에 데이터를 입력해줄 방법이 없다. 터미널 환경을 아톰 에디터를 통해 설치하거나 cmd(명령 프롬포트)를 통해 실습해도 좋다.

# cmd를 통해 실습할 때는 파이썬 파일의 위치를 알아햐 나느데 순서는 cd \  ->  cd python_basic -> dir(디렉터리) -> python(파이썬이라는 명령을 붙여야 한다.) chapter05_02.py 후 입력하면 인터프리터가 한줄 한줄 해석하는 것이다.

# 예제 2

number = input("Enter number : ")

name = input("Enter name : ")

print("type of number", type(number), number*3)

print("type of name", type(name))

# 입력 받은 데이터들의 자료형을 확인해보면 모두 str문자형으로 출력된다. number*3의 출력 결과는 5를 입력했다는 가정 하에 555라는 값을 출력한다. 5를 정수형 즉 숫자로 인식한 것이 아닌 5를 문자로 인식해 5를 세 번 뽑아낸 것이다. 여기서 알 수 있듯이 input 입력은 무조건 문자형이라는 사실을 유의하자★

# 예제 3(계산)

first_number=int(input("Eneter Number1 : "))

second_number=int(input("Eneter Number2 : "))

# input은 입력받은 데이터를 문자형으로 인식하기 때문에 정수형으로 사용하기 위해서는 정수형 형변환이 필요하다.

total=first_number+second_number

print("first_number + second_number : ", total)



# 예제4(실수형 형변환)

float_number=float(input("Enter a float number : "))

print("input float : ", float_number)

print("input type : ", type(float_number))

# 예제 5

print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : "))

# print문에서 바로 input을 통해 입력 가능(테스트 할 때도 많이 사용한다.) print문도 함수이기 때문에 함수 안에서도 사용 가능한 input

# print문에서 {0} {1} 중괄호 안 숫자들은 뒤 인자들의 매칭 순서임을 알아두자.

# 입력문은 Idle(파이썬 셀) 프로그램을 통해 바로 테스트 가능하다.
