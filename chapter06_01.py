# 객체지향프로그래밍 = OOP

# 객체지향이 왜 필요한가? = 기타 언어에에서도 지원하고 장점을 살펴보자

# 생산성의 향상 : 절차지향(위에서부터 아래로 내려오는 코딩)에 비해 객체지향을 도입하니 생산성이 향상

# 연필, 책, 자동차 등 눈에 보이는 사물들을 객체화시킬수 있다.

# 메소드와 마찬가지로 재사용이 가능 재사용을 극대화시키기 때문에 클래스 기반으로 코딩을 많이 한다

# 상속이라는 개념 클래스 형태로 개발하면 코드의 재사용을 용이하게 할 수 있다.= 개선, 수정, 유지보수가 용이하고 주변에 미치는 악영향(사이드 이펙트)을 최소화시킬 수 있다. 따라서 경제적이다.

# 하지만 경우에 따라서는 객체지향이 무조건 빠른 건 아니다. 절차지향이 더 빠른 경우도 존재한다.

# 클래스는 붕어빵 기계? = 반죽을 붕어빵 틀(기계)에 넣고 작동시키면 붕어빵 모양의 빵이 나오듯 틀을 클래스라 이해하자.

# Chapter06-1

# 파이썬 클래스

# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 네임스페이스 : 객체를 인스턴스화 할 때 저장돤 공간

# 클래스 변수 : 직접 접근 가능 (밑의 dog 클래스로 예를 들면 dog class를 이용해서 강아지를 1000마리 만들어도 species는 'firstdog'로 모두 같다. 하나만 선언되어 있으니까)

# 인스턴스 변수 : 객체마다 별도 존재 (하지만 그 강아지 1000마리 마다 self, name, age는 모두 서로 다를 것이다.)(나만의 공간=네임스페이스를 별도로 갖고 있다.)



# 클래스 와 인스턴스 차이를 이해


# 예제1 (애견샵에서 운영하는 소프트웨어를 예로 들어)

# 애완견의 종류는 정말 다양

# 진돗개 =

# 리트리버=

# 이런식으로 변수를 선언하면 견종의 이름이 바뀌거나 새로운 강아지가 추가될 때는 변수가 추가되고 코드가 추가되므로 가독성이 떨어지게 된다 여기서 클래스를 이용하자. 클래스 형태로 구성해보자.

class Dog:

# class(예약어) (사용자가 설정할 class 이름)(object): (object)는 생략 가능하다. object만 생략해도 되고 (object) 째로 생략해도 된다.

# 모든 class는 오브젝트를 상속 받는다.

# 들여쓰기, 콜론은 필수이다.

    # 클래스 속성 지정

    species ='firstdog'

    # 초기화/인스턴스 속성 지정

    def __init__(self, name, age):

    # 모든 클래스는 초기화 메소드를 갖는다.

    # 파이썬은 클래스가 초기화될 때 반드시 한 번 호출되는 함수 __init__가 있다. 첫번째 인자로는 self가 오고 그 디음 이 class를 가지고 사용할 변수나 속성을 지정(여기서는 개(class)의 이름 name 과 나이 age를 지정)

        self.name=name
        self.age=age

        # 위 행들에서 .name, .age 부분은 사용자가 임의대로 지정해 줄 수 있다.
        # 여기서 주의할 점은 지정해준 class에서 사용할 변수와 속성 name , age를 정확하게 매핑하는 것이다.

# 이 calss가 눈에 보이는 개의 종류 이런 것들을 통합하는 객체라고 볼 수 있다. 우리가 만들 소프트웨어로 구현할 대상을 객체라고한다.

# class는 붕어빵 틀이고 인스턴스는 그 틀을 가지고 찍어내는 우리가 코드에서 클래스를 가지고 코드에서 사용하는 어떤 객체라고 생각하면 된다.

# 클래스 정보
print(Dog)



# 인스턴스화

a=Dog("mikky", 2)

# a(임의의 변수)=Dog(class이름)(mikky(사용자가 지정한Dog class의 변수1 ), 2(사용자가 지정한 Dog calss의 변수2)) 참고로 self는 자동으로 넘어온다.

b=Dog("baby", 3)

c=Dog("mikky", 2)

#  .....

# 사용자가 계속 하나의 틀(Dog class)(설계도) 을 가지고 구현된 것을 인스턴스화 되었다고 한다.

# 인스턴스는 코드를 직접 구현해서 메모리에 올라간 그 시점이고 어떤 변수로 활용할 수 있는 대상

# 비교

print(a==b, id(a), id(b), id(c))

# 하나의 같은 클래스를 가지고 인스턴스화 시켰지만 a와 b는 다른 인스턴스다. 같은 name과  age를 갖고 있더라도 인스턴스화시킨 것들은 모두 서로 다른 인스턴스이다.

# 네임스페이스

print("dog1 ", a.__dict__)

print("dog2 ", b.__dict__)

# 이런식으로 코딩하면 dog class의속성을 딕셔너리형으로  확인할 수 있다. 여기서는 name과 age이다. 네임스페이스 = 자기(인스턴스)만의 공간

# 인스턴스 속성 확인

print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

# a와 b를 인스턴스화 시켰으므로 인스턴스 속성에 접근이 가능해진다.

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))



# 클래스 속성 species는 직접접근 가능

print(Dog.species)



# 물론 인스턴스화된 변수로도 접근 가능

print(a.species)

print(b.species)

# species라는 클래스 속성은 공유하는 속성이고 각기 다른 변수들(self)은 name, age와 같이 인스턴스 속성들!

# 예제2
# 예제 2

# self의 이해

class SelfTest:
    def func1():  # 두 개의 메소드(함수)를 호출할 건데 하나는 self가 없는 것 하나는 self가 있는 것
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

# 허나 class를 선언 할 때 꼭 실행되는 함수 __init__은? 이것은 파이썬이 __init__가 없으면 내부적으로 알아서 생성해 실행한다. 여기서는 따로 필요한 name, age같은 인스턴스 속성이 필요 없기에 기본으로 사용할 것이기 때문에

f=SelfTest()

# 인스턴스 지정 과정, = a(임의의 변수)=Dog(class 이름)(mikky, 2)를 생각하자.
# f(임의의 변수)=SelfTest(class 이름)()(빈 칸인 이유는 기본으로 설정했기에 즉 따로 지정시켜준 인스턴스 속성이 없기 때문에 빈칸이다.)

# print(dir(f))

# dir은 사용할 수 있는 메소드를 보여주는 데 여기서 func1, func2가 들어가 있다는 점을 알아두자.

print(id(f))

# f.func1() 예외 = 오류발생

# f.finc1()을 실행하면 에러가 발생한다. 그 이유는 func1은 self가 없는 즉 매개변수가 아무것도 없는 데 하나가 넘어와서 에러가 발생한 것이다.

f.func2()

# self는 인스턴스를 요구한다. 즉 def func2(self)의 self에 f가 넘어가 것이다.

# 위 print(id(self))의 값과 print(f)의 값이 같다는 것을 파악할 수 있다.

# 즉 암묵적으로 클래스(SelfTest) 내부의 매개 변수를 선언하는데 self가 없는 것은 클래스 메소드이다.(즉, Dog class로 예를 들면 species='firstdog')  self가 있는 것은 인스턴스 메소드

SelfTest.func1()

# func1(클래스 메소드)을 호출할 수 있는 코드이다. SelfTest(클래스 이름).func1(클래스 메소드)() 호출되어서 func1()의 하위구문 print('Func1 called')가 출력되었다.

# Dog class로 예를 들면 Dog.species이다.

# SelfTest.func2() 예외 발생

SelfTest.func2(f)

# 반대로 SelfTest(클래스)의 func2을 실행시키면 에러가 발생한다. func2는 하나의 매개변수를 필요로 하는데 들어가 있지 않아서 에러가 발생한 것이다. 여기서 ()안에 f를 넣어 실행하면 정상 작동한다. 이는 매개변수로 인스턴스화 시킨 변수 f를 넣었기 때문이다.

# 즉 클래스로 바로 접근을 해서 호출할 때 self가 없다면 인스턴스화된 변수를 인자로 넣어서 실행시키면 되고 인스턴스화 시켜서 호출(f.func2())시키면 def  func2(self)의 self로 f가 넘어가서 호출된다.

# 예제 3

# 클래스 변수(공유 속성), 인스턴스 변수(자신만의 속성)

class Warehouse:

    # 클래스 변수

    stock_num = 0  # stock를 재고라 하자.

    def __init__(self, name):

        # 인스턴스 변수

        self.name=name

        Warehouse.stock_num +=1

        # 위 코드는 객체가 하나 만들어질 때마다  Warehouse(클래스)의 stock_num(공통 속성)을 하나씩 추가하겠다는 의미이다.

    def __del__(self):
        Warehouse.stock_num -= 1

user1=Warehouse('Lee')

# 인스턴스화된 변수 생성 user1(변수)=Warehouse(클래스)('Lee')(인스턴스 속성 name에 해당하는 값)

user2=Warehouse('Park')

print(Warehouse.stock_num)

# 위 print문은 Warehouse 클래스의 공통 속성 stock_num의 수를 파악하기 위한 기능을 하고 있다. 예상하는 바로는 인스턴스 2개(user1, user2)가 추가되었기 때문에 2의 결과가 나올 것이다.

# 두 번 인스턴스화 시켰으므로 __init__함수가 2번 호출되었다는 의미이므로 함수의 하위구문 Warehouse.stock_num += 1이 두번 호출되었음을 알 수 있다.

#  각 인스턴스에 접근

print(user1.name)

print(user2.name)

# 각 인스턴스들의 네임스페이스에 접근

print(user1.__dict__)

print(user2.__dict__)

# Warehouse 클래스의 네임스페이스에 접근

print(Warehouse.__dict__)

# 이를 통해 stock_num=2로 바뀐 것을 파악할 수 있다. 하지만 stock_num은 클래스 메소드(공통속성)로 공유한다 하였는데 user1과 user2의 네임스페이스에는 출력되지 않은 것일까? 이는 어차피 모두가 공유하므로 표시하지 않은 것이다.

print(user1.stock_num)

# 인스턴스에 공통속성(클래스 메소그)을 확인하고 싶다면 user1(인스턴스화된 변수).stock_num(클래스 메소드)로 코드를 짜보도록 하자.

del user1

# user1을 메모리에서 할당해제(제거)

print('after', Warehouse.__dict__)

# del을 이용하여 메모리에서 user1을 제거시키니 stock_num=2에서 1로 바뀌어 있다. 이는 def __del__(self): 가 호출되어 하위구문에 의해 stock_num이 -1된 것이다.
# 예제4

class Dog1: # object 상속

    # 클래스 속성

    species='firstdog'

    # 인스턴스 속성

    def __init__(self, name, age):

        self.name=name

        self.age=age

# 입력 받은 name, age를 각각 self.name, self.age에 저장

# 클래스 내 메소드(함수) 만들기(위에 SelfTest 클래스의 func1, func2 처럼 )

    def info(self):

        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):

        return "{} says {}!".format(self.name, sound)

 # speak 함수(메소드)를 호출할 때 sound를 입력 받아서 하위구문의 sound에 대입해서 출력

# 초반 Dog 클래스와 다르게 가지고 있는 공통속성(클래스 메소드 species) 그리고 인스턴스 메소드(name, age) 개가 하는 행동(동적인 것)을 추가한 class라고 볼 수 있다.

# 인스턴스(프로그램에서 사용할 객체) 생성

c=Dog1('july', 4)

d=Dog1('Marry', 10)

# 메소드 호출

print(c.info())

#  info 메소드는 문자열을 리턴하므로 print문을 이용했다.

# 메소드 호출

print(c.speak('Wal Wal'))

print(d.speak('Mung Mung'))

# 여기서 self.name는 'july'로 넘어가지만  sound는 없기 때문에(4는 self.age에 저장되어있다.) 우리가 넘겨줘야 한다. 따라서 'Wal Wal' 대입

# 여기서 self의 id값과 c의 id값을 같다.

# 이렇게 하나의 클래스를 이용해서 여러가지 종류로 인스턴스(자기만의 정보를 가짐)로 만들어서 재사용이 가능 말하는 방식이 다르므로 speak 메소드로 다르게 구현

# Self는 인스턴스화된 변수
# 인스턴스 메소드는 self를 인자로 받는 것들(여기서는 __init__,  info, speak)
# 인스턴스 변수는 self를 붙이고 선언하는 변수들 (self.name, self.age)
