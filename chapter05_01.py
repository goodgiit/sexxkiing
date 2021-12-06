# Chapter05-1

# 파이썬 함수 및 중요성

# 파이썬 함수식 및 람다(Lamda)

# 함수의 장점 : 복잡해진 프로그램을 단게별로 나눠 함수단위로 생각해 프로그램의 흐름을 풀어나갈 수 있다.

# 두번재로는 코드의 재사용성이다. 모든 프로그램 기능들은 분리되고 모듈화된 기능들은 함수를 통해 실행하면 코드의 재사용성이 좋아진다.

# 세번째로는 코드의 안정성이 좋아지고(하나에만 집중하기 때문에) 하나의 관심사에 집중할 수 있다. 에러 수정하기에도 용이

# 함수 정의 방법

# def function_name(변수이름)(parameter)(인수):(콜론) 파라미터가 없는 함수도 있고 function을 축약해 func로 많이 쓴다. 함수 내부에서 쓸 인수는 임의대로 , 또한 들여쓰기도 필요하다.

#    code(코드)



# 예제1

def first_func(w):
    print("Hello, ", w)

# w(매개변수)가 없어도 된다.

word="Goodboy"
first_func(word)  # 인수 없이 실행하면 에러가 발생한다.

# 인수에 word를 넣고 실행하면 word가 w위치에 들어가서 print("Hello, ", w)에서 출력이 되는 것이다. 그래서 w를 매개변수로 지칭하는 것이다. 외부에서 호출하는 것

# 참고로 first_func()에서 괄호 없이 실행하면 아무일도 일어나지 않는다 왜냐? func자체가 파이썬 내에 하나의 아이디값을 가지고 있는  func 객체이기 때문이다.

# 예제2(리턴문)

def return_func(w):
    value="Hello, "+ str(w)  # w에 숫자가 올 수 있으므로 문자형 + 문자형을 해줘야 하므로 문자형 형변환이 이루어지고 있다.
    return value

# return 하고자 하는 값을 중간에 변수value를 선언해서 값을 만들고 return하는 방식이 정석이다.

# 깔끔한 방식은

# def return_func(w):
#     return "Hello, " + str(w)

# 이렇게 해도 에러없이 실행된다.

x=return_func('Goodboy2')
print(x)

# 예제1은 print문을 호출한 것이지만 예제2는 내가 원하는 값(value)을 만들어서 반환받아 x를 호출한 것이다.

# 예제3(다중반환)

def func_mul(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return y1, y2, y3

x, y, z=func_mul(10)  # 3개를 리턴(y1, y2, y3)하기 때문에 받는 쪽(x, y, z)도 3개가 필요하다. => 언팩킹
print(x, y, z)

#  다중 반환은 파이썬의 큰 장점이다.

# 튜플 리턴

def func_mul1(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return (y1, y2, y3)  # 위의 다중반환과의 차이점 : 반환값들을 ()튜플로 팩킹함

q=func_mul1(20)
print(type(q), q, list(q))

# 반환 값들을 소괄호로 묶어 팩킹했을 뿐인데 반환되어 나오는 값들 또한 팩킹(튜플형)되어 출력된다. 당연하게 리스트형이 필요하다면 리스트형변환을 통해 얻어낼 수 있다.



# 리스트 리턴

def func_mul2(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return [y1, y2, y3]

p=func_mul2(30)
print(type(p), p, set(q))

# 이번에는 리턴 값들을 []로 묶었는데 리턴되어 나오는 값들이 리스트형으로 출력되었다. 물론 set형이 필요 시 set형변환을 통해 얻을 수 있다.

# 딕셔너리 리턴

def func_mul3(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return {'v1' : y1,'v2' : y2, 'v3' : y3}  # 딕셔너리는 키와 밸류 값들로 이루어졌기 때문에 그냥 중괄호{}만 치면 set형으로 반횐되어 나올 것이다. 따라서 임의대로 키를 만들어 처리해야 한다.

d=func_mul3(30)
print(type(d), d, d.get('v1'), d.items(), d.keys())



# 함수형 프로그래밍 일반 명령형 프로그래밍을 공부해보도록 하자.

# 중요
# *args, **kwargs (매개변수 안에 들어감)

# *args(언팩킹)(★)

def args_func(*args): # 매개변수 이름은 자유
# *args는 가변(★)이라는 의미이다. *args는 매개변수로서 들어오는 값이 몇개이든 그 횟수만큼 풀어서 반복문을 사용하겠다는 의미이다. 튜플형태가 들어올 때 많이 사용한다.
    for i, v in enumerate(args):  # i,v 는 임의대로 지어도 되지만 여기서의 i는 index v는 실제 값을 의미하게 해주는 enumerate 함수
        print('Result : {}'.format(i), v)
print('-----')

args_func('Lee')
# 만약 args_func('Lee')으로 'Lee' 하나만 있었다면 *args가 아니어도 (args) 실행가능하다. 단 'L', 'e', 'e' 하나의 문자형으로 인식해 각각 튜플형태의 0번 1번 2번 index로 인식하겠다는 것이다.
args_func('Lee', 'Park')
# 함수를 선언할 때 인자가 두개면  갯수만큼 매개변수가 2개이어야 하는데 *argss는 보내는 것들을 묶어서 보낸다고 생각하고 안에서 enumerate를 통해 풀어버린다. 즉 'Lee', 'Park' 각각 0번 1번 index로 인식한다. 따라서 ('Lee', 'Park')를 하나의 튜플로 인식하고 있다는 것이다.
args_func('Lee', 'Park', 'Kim')

# 물론 함수 안에 원소는 100개 그 이상도 될수 있다. *args는 함수를 유연하게 사용할 때 이용한다.

# **keargs(언팩킹)(딕셔너리 자료형 언팩킹)(★)

def kwargs_func(**kwargs):  # **이 중요한 것이다. 매개변수 명은 자유다.
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v]) #.format(v)는 키의 값이 {}안에 들어갈 것이고 kwargs[v]를 통해 밸류값이 출력될 것이다.(get메소드가 아닌 속성을 통해 밸류값에 접근한 방법)
print('------')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Kim')

# **인것은 딕셔너리형 = 키와 밸류값으로 이루어진 것들을 매개변수로 넘길 때 사용한다.(★)

# 딕셔너리형의 원소 수에 따라 반복문의 반복횟수가 정해진다. 원소의 개수가 name1='Lee' 하나일 때는 한 번 반복하였지만 원소의 개수가 2개(name1='Lee', nmae2='Park' )일 땐 두 번 반복하는 모습을 볼 수 있다.

# 핵심은  딕셔너리형을 보내면 반복문 안에서 풀어서(언팩킹) 접근할 수 있도록 하는 것이다.(★)


# 전체 혼합

def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age=30, age3=40)

# 먼저 10, 20은 어디에 할당이 될까? 10과 20은 인자 순서대로 args_1, args_2에 할당이 되고 그다음  'Lee', 'Kim', 'Park'는 가변매개변수 *args에 할당이 되어 하나의 튜플형으로 반환되어 출력된다. 여기서는 총 3개의 원소가 할당되지만 더 많이 있었어도 할당되었다. 그 다음 키와 밸류 형태로 이루어진 age1=20, age=30, age3=40은 딕셔너리형 매개변수 **kwargs에 할당이 되어 하나의 딕셔너리형으로 취급되어 출력된다.

# 인수의 갯수에 구애받지 않고 함수를 원하는 형태로 폭 넓게  유연하게 쓸 수 있다.

# 중첩 함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num+100)

nested_func(100)

# 주의할 점은 함수 안의 함수 func_in_func를 외부에서 선언하면 에러가 발생한다.
# 진행과정은 처음 nested_func(100)에 의해 num에 100이 들어가 부모 함수 nested_func이 실행되어 func_in_func도 실행이 가능해진다.
# 먼저 print("In func")이 실행되고 그 다음으 def nested_func의 하위구문 func_in_func(num+100)이 실행되어 def func_in_func(num):의 num은 200이 된다.
# 이러면 def nested_func(num): 부모함수의 실행이 모두 끝난 다음 자식함수 func_in_func이 실행되어 print(num)이 작동해 200을 출력하는 것이다.

# 람다식 예제

# 메모리 절약, 가독성 향상, 코드 간결
# 일반적인 함수는 객체 생성->후  리소스(메모리)할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 후 메모리 초기화 (효율적 메모리 사용가능)
# 남발 시 가독성 오히려 감소

# 일반적인 함수식 할당

# def mul_func(x, y)
#     return x*y

# 람다식(기능은 위 함수식과 같다.)할당

# {a =}lambda x, y: x*y   # x, y는 인자 : 뒤에는 반환되는 양식(x*y)
# {a=(5, 6)}

# 함수의 이름(mul_func)이 없으므로 변수에 담아서 쓰곤 해야 한다.{}는 생략 가능

def mul_func(x, y):
    return x*y

q=mul_func(10, 50) # 임의의 변수 q에 받아서 해도 되고
print(q)  # 바로 print(mul_func(10, 50))을 이용해도 좋다.

mul_func_var=mul_func # 일반적인 함수는 이름이 있으므로 객체가 만들어지고
print(mul_func_var(20, 50)) # 메모리가 할당되어 실행된다.

lambda_mul_func=lambda x, y:x*y # 하지만 람다식은 바로 변수에 할당되어 있고
print(lambda_mul_func(50, 50)) # 바로 출력이 가능하다.

# 람다식은 익명함수이므로 변수(lambda_mul_func)에 담았다.

# 일반적인 함수식을 사용하면 이름만 보고 용도를 파악하기 용이하다. 람다식을 사용하면 처리능력에 있어 더 빠르다.

def func_final(x, y, func):
    print(x*y*func(100, 100))

func_final(10, 20, lambda x,y:x*y )

# 위 func_final 함수는 3개의 인자가 필요하다. 여기서 주의할 점은 마지막 인자를 함수로 받아야 한다. 그 받은 함수에 100과 100을 인자로 넣어서 나온 값과  나머지 받은 2개의 인자 x, y를 곱하는 것이 func_final함수의 기능이다. 여기서 함수를 인자로 받으므로 즉시 실행 가능한 람다식(익명 함수)을 이용한 것이다.

# 또한 위에서 미리 만들어 놓은 람다식을 담은 변수 lambda_mul_func를 인자로 넣어도 되고 또한 일반함수가 담겨있는 변수인 mul_func_var을 넣어도 실행 가능하다.
