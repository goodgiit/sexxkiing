# Chapter03-2

# 파이썬 문자형

# 문자형 중요




# 문자열 생성

str1="I am Python"

str2='Python'

str3="""How are you?"""

str4='''Thank you'''



print(type(str1), type(str2), type(str3), type(str4))

print(len(str1), len(str2), len(str3), len(str4))

# 문자열의 길이를 측정하기 위한 함수 len



# 빈 문자열

str1_t1='' # 빈 문자열로 선언

str2_t2=str() # 이것도 빈문자열로 선언

print(type(str1_t1), len(str1_t1))

print(type(str2_t2), len(str2_t2))


# 빈 문자열의 길이는 0이다.


# 이스케이프 문자 사용 (탈출 문자)

# I'm Boy

print("I'm Boy")

# print('I'm Boy')는 에러가 발생한다 그 이유는 'I'의 작은 따옴표 한 쌍이 있지만 'I'm Boy'에 끝의 작은 따옴표 ' 는 짝이 없기 때문에 에러가 발생한다. 따라서 작은따옴표를 안에 쓰기 위해서는 큰따옴표를  쓰는 것이 좋다.

# 그렇다면 작은따옴표를 쓸려면 어떻게 해야 할까?

print('I\'m Boy')

# 엔터키 위에있는 역 슬러쉬를 이용하면 \ 뒤에 특수기호(')는 그대로 표시가 된다.

# 또 다른 특수기호의 예

print('I\\m Boy')

print('a \t b') # 이는 키보드의 Tab키만큼 a와 b사이의 간격이 벌어진다.

print('a \n b') # 이는 a와 b를 줄바꿈 하는 기능이있다.

print('a \"\" b')

"""

참고 : Escape 코드

\n : 개행

\t : 탭

\\ : 문자

\' : 문자

\" : 문자

\000 : 널 문자

...

"""

escape_str1="Do you have a \" retro games\"?"

print(escape_str1)

escape_str2='What\'s on TV?'

print(escape_str2)

# 탭, 줄 바꿈

t_s1= "Click \t Start!"

t_s2= "New Line \n Check!"

print(t_s1)

print(t_s2)

print()

# 파이썬은 띄어쓰기에 민감하다 따라서 행의 첫 시작에 공백이 존재하면 안된다.

# Raw String 출력 (있는 그대로를 출력) 소문자'r'이 붙어있으면 Raw String이구나 이스케이프 문자를 사용하지 않기 위해 변수를 선언했구나를 생각하자.

raw_s1=r'D:\python\test'

raw_s2=r'D:\tpython\test' # (\t라는 이스케이프 문자가 있어도 그대로를 출력한다.)

print(raw_s1)

print(raw_s2)

# 이는 드라이브 경로를 이용해 파일을 복사한다든지 쓸 때 사용한다.


# 멀티라인 입력
# 역슬래쉬 \ 사용

multi_str="sdfghhgkshjdjkfhjkshfkauhfkajfnkasbjdkashduhawkjdnjkanwdknbjkwqbdjkbwjqkbkbwfqjqkfnqfq"

# 멀티라인은  이렇게 긴 텍스트를 보기 좋게 처리하기 위해 사용된다.
# 작은따옴표 , 큰따옴표 모두 가능

# 이렇게 선언만 헤도 에러가 발생한다 즉 문법 오류 
# multi_str_error=
#'''
#String
#Multi Line
#Test
#'''


multi_str_1= '''

String
Multi line
Test

'''

# 또는 더 나은 예를 위하여

multi_str_2= \
'''
String

Multi Line

Test
'''

print(multi_str_1)
print(multi_str_2)

# 파이썬에서 \는 \ 다음에 오는 어떤 변수를 바인딩에 의미가 있다. 이는 선언할 떄 길게 이어나갈수가 있다.

asdf=\
'dfdfdf'\
'dfdfdf'\

print(asdf)

# 파이썬은 공백에 민감하다. 멀티라인을 실행했을 때 변수 사이의 공백(Multi Line과 Test사이의)이 생겨 실행 에러가 낫었다. 하지만 다시 해보면 안나네..
# 멀티라인을 할 때 따옴표로 묶어야 실행 가능

# 문자열 연산

str_o1="Python"
str_o2="Apple"
str_o3="How are you doing"
str_o4="Seoul Daejeon Busan Jinju"


print(str_o1*3)
# 문자열에 어떤 수를 곱하게 되면 곱한 만큼 문자열이 반복되어 출력된다.
print(str_o1+str_o2)
# 문자열의 합은 서로 이어져 나오게 된다
print('y' in str_o1)
# 'y'라는 문자가 str_o1에 있느냐(포함되있느냐)를 묻는 연산자 'Python'에서 알파벳 하나하나가 리스트라고 생각하면 된다. 시퀀스 데이터형( str , list, tuple)은 in 연산자
print('z' in str_o1)
# True가 1 False는 0
print('P' not in str_o2)
# 대소문자 구분하고 위 행은 'P'가 str_o2에 없느냐를 묻는 연산자이므로  True의 값이 나오게 된다.
print()

# 문자열 형 변환

print(str(66)), type(str(66))
# 보이는 건 66 따옴표가 없어 정수형으로 오해할 수 있지만 type 연산자를 통해 데이터 타입을 알아본 결과 str 문자형 66임을 알 수 있다.
print(str(10.1))

print((str(True)), type(str(True)))
# 중요한 사실! print문이 하늘색이면 맞게 쓴거지만 갑자기 보라색이다? 문제가 있는것이다.
# 특히 syntaxerror: unexpected eof while parsing의 오류시 괄호의 쌍이 맞는지를 체크해야한다! + 따옴표 , 철자
print()
# 문자열 함수(upper, isalnum, startswith, count, endwith, isalpha ...)
print("Capitalize: ", str_o1.capitalize())
# 이 함수는 첫글자를 대문자로 바꾸는 함수이다.

print("endswith?: ", str_o2.endswith("e"))

# 이 함수는 마지막 문자가 무엇이냐를 묻는 함수이다 위행에서는 str_o2의 마지막 문자가 "e"로 끝나는지를 묻고있다. ! 나 . 도 가능
# endwith가 아닌 endswith!

print("replace", str_o1.replace("thon",'Good'))

# replace함수는 문자열을 바꿔주는 역할을 하는 함수이다.

#위 행에서는 str_o1의 Python의 thon을 Good으로 바꿔주었다. 물론 바꿔주는 단어에 띄어쓰기 포함 가능

print("sorted: ", sorted(str_o1))

# 문자열을 어떤 기준에 맞게 리스트 형태로 반환해주는 역할을 한다.

print("split: ", str_o4.split(" "))

# split 함수는  파라미터 안에 인자(여기선 공백)를 기준으로 분리시켜주는 각각의 단어를 리스트 배열 형태로 반환해주는 기능을 가진 함수이다.

# 반복(시퀀스)

im_str="Good Boy!"

print(dir(im_str))

# 일단 이 함수 dir은 im_str에서 사용할 수 있는 모든 것들을 나열해주는 함수 여기서 __iter__를 주목해야 하는데 이는 시퀀스(반복)가 가능하다는 것이다.

for i in im_str:
    print(im_str)

# 문자열은 시퀀스형이라 슬라이싱 처리가 가능하다.
# 슬라이싱

str_s1= "Nice Python"

# 슬라이싱 연습

print(str_s1[0:3])

# 여기서 "Nice Python"에서 N이 0번부터 시작해서 n이 10번으로 끝나(공백 포함) 총 11글자이다. 위 행은 0번부터 3번인 e까지가 아닌 0번(N)부터 (3-1)=2번인 c까지 나와 결과는 Nic가 출력된다.

print(str_s1[5:])  # =[5:11] 빈칸으로하면 끝까지 출력

# 첫 시작은 0번부터라는 점을 유의하자 또 뒤에 숫자는 -1이된다는 사실 또한 알아두자.

print(str_s1[:len(str_s1)]) # len(str_s1)=11이므로 이는 [0:11]과 같다. 끝부분의 길이를 모를 떄 사용

print(str_s1[:len(str_s1)-1])  # str_sl[:10]

print(str_s1[1:9:2])

# 이는 str_s1의 문자열 이 1번(i)부터 8번(t)까지 (세번째 인수는 단위)2개씩 점프(스킵)해 가져오라는 의미의 함수이다. 따라서 ie가 디버깅된다. { i(c)e()P(y)t(h)} [ ()는 생략하는 것들 가 출력 ]

print(str_s1[1:9:3])

print(str_s1[4:10:3])

print(str_s1[-5:])

# 음수일 시에는 문자열의 오른쪽 끝부터 -1번이  된다. 결과는 ython이 나오게 되는데 번호만 역순으로 매겨지지 진행방향은 오른쪽으로임을 유의하자.

print(str_s1[1:-2])

# 부호가 달라도 사용 가능 1번(i) -2번(o) 물론 여기서도 -2 -1 = -3이라는 사실을 유의하자.

print(str_s1[::2])

# 생략된것들은 처음부터 끝까지를 의미하는 것이고 마지막 인수가 2이기 때문에 스킵 점프하는 단위는 2가 된다. 따라서
# { N(i)c(e) (p)y(t)h(o)n }이 출력 된다.  물론()들은 스킵된 것들이고 (e)와(p) 사이의 공백은 살아있다. 공백도 번호를 차지하기 떄문
print(str_s1[::-1])

# 이는 처음부터 끝까지 점프(스킵)가 -1이다? 이는 역순으로 처음부터 끝까지를 출력한 것과 같다.

# 긴 문자열에서 특정 단어만 뽑아내는 역할을 할 수있는 슬라이싱

# 아스키 코드(또는 유니코드)

a='z'

# 파이썬에서 처리되기 위해 각 문자는 아스키 코드로 처리되어있다. 각 해당번호가 있다.

print(ord(a))

# ord 함수는 (위에서는) a에 할당된 문자의 아스키코드 즉 z=122번임을 보여주고 있다.

print(chr(122))

# chr함수는 반대로 아스키코드에 해당하는 문자를 보여준다. 122=z
