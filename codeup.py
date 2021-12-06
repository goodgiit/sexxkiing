# print("\"!@#$%^&*()\'")
# print("\"!@#$%^&*()\'")
# print("\"!@#$%^&*()\'")



# print('print("Hello\\nWorld")')

# # 파이썬의 이미 있는 기능이 있는 문자(ex : \n, '', "", #, /,...)가 아닌 이상  따옴표들의 쌍 안에 써주면 특수문자 출력 가능!

# f=float(input())
# print(f)

# # f=input(float())
# # print(f)
# #  위향과 다르게 밑의 행은 float()를 먼저 실행하기 때문에 괄호 안에 아무것도 없기 떄문에 예와가 발생한다.

# a='Kim'
# for i in range(3):
#     print(a)

# # 6016
# a, b=input().split() # 공백을 기준으로 a, b변수에 대입하고 싶을 때 여기서 split의 인자에 아무것도 들어가지 않아야 한다.(따옴표 ''도 X)
# print(b)
# print(a)

# 6017
# a=input()
# print(a, end='')
# print(a, end='')
# print(a, end='')

# a=input()
# for i in range(3):
#     print(a, end=' ')

# 6017
# x=input().split(':')
# print(x, sep=':')

# 한 변수에만 split()을 하고 print문 sep=split()의 같은 문자로 구분할 시 리스트형의 두 원소로 쪼개져 출력된다.

# 6018
# x, y=input().split(':')
# print(x, y, sep=':')

# 6017과의 차이점을 인식하자.

# split의 인자에는 구분해주고자 하는 것이 들어가야하는 데 문자이면 꼭 따옴표 안에 넣어주자!
# sep의 기능은 print의 인자(x, y)는 ,로 구분되어 있는데 이 구분을 무엇으로 표시할 것이냐라는 기능을 가졌다 여기서는 ':'이기 때문에 x와 y의 구분을 :로 처리하고 있다.

# 6019
# y, m, d=input().split('.')
# print(d, m, y, sep='-')

# split의 기능은 어떤 인자로 입력받은 변수를 구분할 것인가~ 이다. 꼭 문자열이면 따옴표 안에 넣어주는 것에 유의하자.

# 6020
# f, b=input().split('-')
# print(f,b, sep='')

# 공백으로 print문의 인자들을 구별하겠다는 것은 그냥 빈 칸이 없게 인자들을 표시하겠다는 것이다.

# 6021
# a=input()
# print(a[0], a[1], a[2], a[3], a[4])

# 문자(str)형 또한 iterable이기 때문에 각 글자마다 index가 존재한다.

# 6022
# a=input()
# print(a[:2],a[2:4],a[4:6])

# print문을 엔터키 치지 않고 한 행안에서 ,처리를 하면 
# 공백(띄어쓰기)을 기준으로 각 인자들이 구분된다.

# 6023
# h,m,s=input().split(':')
# print(m)

# 6024
# a,b=input().split()
# print(a,b,sep='')

# 6024 (정석)
# a,b=input().split()
# print(a+b)

# + 연산을 통해 a,b 사이의 공백을 처리할 수 있다. 또한 sep=''를 통해서도 입력받은 두 단어를 이어붙이기가 가능하다.

# 6025
# i1,i2=input().split()
# sum=int(i1)+int(i2)
# print(sum)

# 6025 예외 발생 예 
# i1,i2=int(input().split())
# print(i1+i2)
# 한 번에 처리하기 위해선 map함수 이용

# i1,i2=input().split()
# int(i1)
# int(i2)
# print(i1+i2)

# 6026
# f1=input()
# f2=input()
# sumf=float(f1)+float(f2)
# print(sumf)

# 줄을 바꿔서 입력하고 싶으면 위와 같이 줄을 바꿔 input에 대한 변수를 선언해주면 된다


# 6027

# a=input()
# a=int(a)
# print('%x'% a)

# 16진수 표현법은 %x이다.(8진수 표현법은 %o)
# 여기서는 print문 안에 % 대응법을 알아두자. 

# 6028

# a=input()
# a=int(a)
# print('%X'% a)

# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f)인데 문자들을 대문자로 표현하기 위해서는 %X 를 이용한다. 
# 물론 8진수도 %O로 가능하다.
# 같은 변수를 써서 재할당 가능

# 6029

# a=input()
# a=int(a, 16)
# print('%o'% a)

# 16진수로 입력받고 싶다면 int형변환 인자 뒤에 16 인자를 추가하여야 한다.
# 물론 8진수로 입력받고 싶다면 인자에 8 추가

# 6030
# str1=input()
# print(ord(str1))

# 아스키 코드(유니코드) 문자를 입력 받았는데 '그에 맞는' 정수로 전환하고 싶을 때 사용할 수 있는 ord( 그 문자에 맞는 아스키코드 출력)

# 6031
# str2=input()
# str2=int(str2)
# print(chr(str2))

# chr(은 반대로 아스키 코드(유니코드)에 해당하는 문자를 출력한다.)

# 6032

# x=input()
# x=int(x)
# print(-x)

# 입력 받은 수의 부호를 바꾸고 싶다면 간편하게 부호를 붙여 출력하면 된다.

# 6033 ★

# x=input()
# x=ord(x)
# print(chr(x+1))

# 일반적으로 input은 문자열을 입력받는다
# 그러므로 일반적인 문자열(숫자로 이루어진 문자열이 아닌..)을 int형 변환하는 것은 불가능하지만
# 문자를 그에 맞는 아스키코드(유니코드) [정수]로 바꿔줄 수는 있다. 바로 ord를 통해


# 6034

# a1,a2=input().split()
# a1,a2=int(a1), int(a2)
# print(a1-a2)

# 형변환을 ,를 이용해 한 행에 쓸 수 있다.

# 6035

# f1,f2=input().split()
# f1=float(f1)
# f2=float(f2)
# print(f1*f2)

# 6036

# str1,count1= input().split()
# count2=int(count1)
# print(str1*count2)

# 6037

# c=input()
# s=input()
# is1=int(c)
# print(s*is1)

# 네이밍 할 때 꼭 뭐가 뭔지 파악하고 계산하도록 하자.
#  위에서는 c=count(횟수), s=str(문자)

# 6038

# a,b=input().split()
# a,b=int(a), int(b)
# print(pow(a,b))

# 꼭 input은 문자열로 입력받는 사실을 유의하도록 하자. 정수형 계산이 필요 할 땐 꼭 정수형변환 필요!
# pow는 거듭제곱의 기능이 있다. ex) pow(a,b)= a에 b제곱(승)의 계산을 한다.

# 6038-2

# a,b=input().split()
# a,b=int(a), int(b)
# print(a**b)

# pow 기능 대신 *를 두번 사용한 **을 사용해도 거듭제곱의 기능을 할 수 있다.

# 6039

# f1,f2=input().split()
# f1=float(f1)
# f2=float(f2)
# print(f1**f2)

# 거듭제곱의 기능을 하는 것은 ** 와 pow()가 있다는 것으 알아두자.

# 6040

# a,b=input().split()
# a=int(a)
# b=int(b)
# print(a//b)

# //는 몫만 출력되게 하는 기능을 가진다.
#  예를 들어 위 코드에 print(a/b)이고 10 3을 입력하면 3.33333..이 나오게되지만 
# //을 통해 3만 나오게 할 수 있다.

# 6041

# a,b=input().split()
# a=int(a)
# b=int(b)
# print(a%b)

# %는 나머지를 출력하게 하는 기능을 가진다. ex) 10%3=1

# 6042 모법 답안

# a=input()
# a=float(a)
# print(format(a,".2f"))

# # 6042 내가 한 답안

# a=input()
# a=float(a)
# print('{:.2f}'.format(a))

# 6042-2

# a=input()
# a=float(a)
# print(round(a,2))

# round 함수를 이용해서 반올림하고 싶은 소수점 아래 자랏수를 조절할 수 있다.
# 위 코드에선 입력받은 실수 a의 소수점 아리 둘째짜리까지 나타내는 기능을 하고 있다.

# 6043

# f1,f2=input().split()
# f1,f2=float(f1), float(f2)
# f3=f1/f2
# print(format(f3,".3f"))

# unexpected EOF while parsing 예외가 발생하면 꼭 괄호를 닫았는 지 끝맺음을 잘 마쳤는지 확인해보자
# 반올림하는 법 3가지를 기억해두자 (모두 f3을 소수점아래 셋째짜리까지 표현하고 싶을 때)
# print(foramt(f3,".3f"))
# print('{:3f}'.format(f3))
# print(round(f3,3))

# 6044 ★


# a,b=input().split()
# a,b=int(a), int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print('{:.2f}'.format(a/b))

# 6045

# a,b,c=input().split()
# a,b,c,=int(a),int(b),int(c)
# print(a+b+c, format((a+b+c)/3,".2f"))

# 3개 이상의 변수도 한 행에서 동시에 선언도 가능, 입력받는 것도 가능
# int형으로 나눈 값을 확인하는 것이 맞는 것 같다.

# Tip
# python 프로그래밍을 처음 배울 때 좋은 습관(단계)
# 1. 입력된 문자열을 정확하게 잘라낸다.(공백, 줄바꿈, 구분문자 등에 따라 정확하게 잘라낸다.)
# 2. 잘라낸 데이터들을 데이터형에 맞게 변환해 변수에 저장한다. (정수, 실수, 문자, 문자열 등에 따라 정확하게 변환한다.)
# 3. 값을 저장했다가 다시 사용하기 위해, 변수를 이용해 값을 저장하고, 변수를 이용해 계산을 한다.
# 4. 원하는 결과 값을 필요한 형태로 만들어 출력한다.(공백, 줄바꿈, 구분자, 등에 따라 원하는 형태로 만들어 출력한다.)


# 6048
 
# a,b=input().split()
# a,b=int(a),int(b)
# print(a<b)

# 조건문 그 자체 ex) print(a<b) 는 출력 값이 True or False이다.
# ★★★ 당연하게도 정수로 크고작음 을 판단하므로 정수형변환 필수!라는 점을 유의하자!

# 6049

# a,b=input().split()
# a,b=int(a),int(b)
# print(a==b)

# 두 인자가 같은 지를 물어보는 연산자는 ==이다. ( = 이아니라)

# 6050

# a,b=input().split()
# a,b=int(a),int(b)
# print(b>=a)

# 6051

# a,b=input().split()
# a,b=int(a),int(b)
# print(a!=b)

# print문의 인자에 조건문이 오면 출력은 True or False로 나오게 된다.
# !='not'의 의미를 담고 있어 a!=b는 'a와 b는 다른가?'를 묻고 있다.

# 6052 ★

# a=int(input())
# print(bool(a))

# a=int(input())처럼 변수가 하나만 있을 때는 한 행에 int형 변환까지 할 수 있다.
# 하지만 변수가 2개 이상일 시 한 행에 split()까지 하는 것은 불가능하다.
# ★ bool형은 True or False를 판단하는 자료형!

# 6053

# a=int(input())
# print(bool(not(a)))

# 파이썬은 !a 로 디버그 시 예외가 발생하므로 not연산자를 사용해주어야 한다.

# 6054

# a,b=input().split()
# a,b=int(a), int(b)
# print(all((bool(a),bool(b))))

# all 함수는 모두 True일 시 True를 출력하는 함수이다.
# all()함수는 ()안에 인자가 하나밖에 오지 못한다. 
# 즉 print(all(bool(a),bool(b))), print(bool(all(a,b)))이런식으론 작성하지 못한다. 
# 이로 보아 all 함수는 ()안 인자가 True or False여야 연산이 가능하다.

# 6054-2 모범답안

# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))

# 모범답안은 and연산자를 통해 모두 참(True)일 때 True를 출력하게하는 것이다.

# 6055

# a,b=input().split()
# a,b=int(a),int(b)
# print(bool(a) or bool(b))

# or연산은 or의 피연산자들 중 하나라도 True(참))깂이 있을 시 True를 출력한다.

# 6055-2

# x,y=input().split()
# x,y=int(x),int(y)
# print(any((bool(x), bool(y))))


# 6056 ★
# a와 b가 서로 다른 경우에만 참(True)값 출력

# a,b=input().split()
# a,b=int(a),int(b)
# print(a!=b)

# 서로 같은 경우에 True(참)값을 출력하는 연산자는 ==
# 서로 다른 경우에 True(참)값을 출력하는 연산자는 !=

# 6056-2

# x,y=input().split()
# x,y=bool(int(x)),bool(int(y))
# print(x and (not(y)) or ((not x) and y))

# x and not(y), not(x) and y 연산을 파헤쳐보면 
# # 만약 입력되는 값들이 같은 값들이라면(if T T, F F) 무조건 위 연산은 F값이 나올 수 밖에 없다.
# 즉 마지막 or연산을 통해 두개의 F가 있으니 같은 bool형의 값이 들어간다면 F가 나올 수 밖에 없다


# 6057

# a,b=input().split()
# a,b=bool(int(a)),bool(int(b))
# print(a==b)

# 프로그래밍을 하면서 한 행마다 목적을 두는 것이 좋다.
# 위 코드들로 예를 들면 첫번째 행은 입력을 위한 행
# 두번째 행은 형 변환을 위한 행
# 세번째 행은 연산과 출력을 위한 행

# 6057-2

# x,y=input().split()
# x,y=bool(int(x)),bool(int(y))
# print((not(x) or y) and (x or not(y)))

# not and or 연산자들로만 가지고 같은 경우에만 참 출력 또는 디른 걍우에만 참 출력을 풀 수 있다.
# 예를 직접 대입해가면서 풀어보자.

# 6058

# a,b=input().split()
# a,b=bool(int(a)),bool(int(b))
# print(not(a) and not(b))

# 6058-2

# x,y=input().split()
# x,y=bool(int(x)),bool(int(y))
# print(not(x or y))

# or연산의 특징(모두 F여야 F출력)을 이용한 코딩

# 6058-3

# p,q=input().split()
# p,q=bool(int(p)), bool(int(q))
# print(p==False and q==False)

# False를 직접 인용해서도 코딩할 수 있다. 6058과 비슷한 의도를 가지고 코딩.

# 6063

# a,b=input().split()
# a,b=int(a),int(b)
# if a>b:
#     print(a)
# else:
#     print(b)

#  6063-2
# ★삼항연산

# x,y=input().split()
# x,y=int(x),int(y)
# z=(x if(x>=y) else y)
# print(z)

# 위 코드에서 z값은 True 또는 False값을 평가할 조건식이다.
# z 변수의 기능은 조건식(x>=y)이 참일 경우 x 그렇지 않을 경우(x<y) y를 출력하게 한다.

# 6064 ★★(세 항 중 가장 작은 항 출력)

# x,y,z=input().split()
# x,y,z=int(x),int(y),int(z)
# v= (x if x<y else y) if((x if(x<y) else y)<z) else z
# print(v)

# 6064-2

# p,q,r=input().split()
# p,q,r=int(p),int(q),int(r)
# print(min(p,q,r))

#  min()을 이용해 쉽게 인자들 중 가장 작은 값을 구할 수 있다.
# 또한 max()를 이용해서도 인자들 중 가장 큰 값을 구할 수 있다.

# 6064-3

# a,b,c=input().split()
# a,b,c=int(a),int(b),int(c)
# d= a if a<b else b
# e= d if d<c else c
# print(e)

# 6064-4

# l,m,n=input().split()
# l,m,n=int(l),int(m),int(n)
# if (l<m):
#     if(l<n):
#         print(l)
#     else:
#         print(n)
#         # l<m인 상태에서 else의 조건은 l>=n
#         # 정리해보면 n=<l<m
# else:
#     # else의 조건은 l>=m
#     # n<m or n>m인 조건이 더 필요하다.
#     if(n<m):
#         print(n)
#     else:
#         # 조건을 정리해보면 m<=l인 상태에서  n>=m이므로
#         # m이 제일 작은 수 임은 확실 나머지 두개(l,n)의 관계는 명확하지 않음
#         print(m)


# 6065

# a,b,c=input().split()
# a,b,c=int(a),int(b),int(c)

# if a%2==0:
#     print(a)
# if b%2==0:
#     print(b)
# if c%2==0:
#     print(c)

# 짝수를 찾는 법은 2로 나눈 나머지가 0이어야 하므로 %2==0임을 이용해야 한다.
# //2 몫을 찾기 때문에 틀린 답이다.

# elif를 이용하면 중간에 짝수를 찾으면 if문을 강제로 탈출하는 것 같다.

# if a%2==0:
#     print(a)
# elif b%2 ==0:
#     print(b)
# elif c%2==0:
#     print(c)
# else:
#     print("짝수 없음")

# 6066

# a,b,c=input().split()
# a,b,c=int(a),int(b),int(c)

# if a%2==0:
#     print("even")
# else:
#     print("odd")

# if b%2==0:
#     print("even")
# else:
#     print("odd")

# if c%2==0:
#     print("even")
# else:
#     print("odd")

# 6067

# a=int(input())

# if a<0 and a%2==0:
#     print('A')
# elif a<0 and a%2==1:
#     print('B')
# elif a>0 and a%2==0:
#     print('C')
# else:
#     print('D')

# elif문은 대입하고자 하는 변수가 하나이면 효율적인 것 같다.

# 6068

# sco=int(input())

# if sco>=90:
#     print('A')
# elif sco>=70:
#     print('B')
# elif sco>=40:
#     print('C')
# else:
#     print('D')

# 6069

# x=input()

# if x=='A':
#     print('best!!!')
# elif x=='B':
#     print('good!!')
# elif x=='C':
#     print('run!')
# elif x=='D':
#     print('slowly~')
# else:
#     print('what?')


# 6070

# 조건문은 조건을 다중으로 쓸 수 없는 것 같다.
# ex) if m==12,1,2:   -> 예외 발생
# 차선책으로 변수에 숫자들을 저장해 한 조건으로 할려 했으나 이것도 안됨/
# ex) if m==winter: -> 예외는 발생하지 않으나 파이썬이 winter 변수 안에 있는 숫자 12,1,2를 인식하지 못한다.

# winter=12,1,2
# spring=3,4,5
# summer=6,7,8
# fall=9,10,11

# m=int(input())

# if m==12:
#     print('winter')
# if m==1:
#     print('winter')
# if m==2:
#     print('winter')
# if m==3:
#     print('spring')
# if m==4:
#     print('spring')
# if m==5:
#     print('spring')
# if m==6:
#     print('summer')
# if m==7:
#     print('summer')
# if m==8:
#     print('summer')
# if m==9:
#     print('fall')
# if m==10:
#     print('fall')
# if m==11:
#     print('fall')

# 6070-2

# m=int(input())

# if m//3==1:
#     print('spring')
# elif m//3==2:
#     print('summer')
# elif m//3==3:
#     print('fall')
# else:
#     print('winter')


# 조건문의 특성을 잘 생각해서 수의 특성도 잘 생각해서 식을 잘 구성해보자.

# 반복문 ★★★
# 6071

# while True:
#     n1=int(input())
#     if n1!=0:
#         print(n1)
#     else:
#         break
    

# 어떻게 해야 한줄만 출력하게 하고 다시 입력받는가
# 그에 대한 답은 while True문안에 n1=int(input())을 넣어 해결
# if조건문 안에 continue문을 안넣어도 while문(무한반복문)이라 가능한 것 같다.

# 6072

# second=int(input())

# while True:
#     if second!=0:
#         print(second)
#         second-=1
#     else:
#         break

# while True문과 if-break문을 이용해서 무한루프를 탈출할 수 있다.

# 6073

# n=int(input())

# while True:
#     if n!=0:
#         print(n-1)
#         n-=1
#     else:
#         break

# 6074 ★★

# al=input()
# al=ord(al)
# a2=97

# while True:
#     if al!=a2:
#         print(chr(a2), end=' ')
#         a2+=1
#     else:
#         print(chr(a2))
#         break

# print문의 인자들을 같은 줄에 띄어서 쓰기 위해서는 
# end=' '를 사용하는데 다른 print문 인자 안에 있더라도 띄어쓰기가 가능하다.
# a의 아스키코드값은 97
# 오름차순으로 출력하기 위해 변수 하나를 또 생성해서 a1=a2의 방식으로 구성했다.

# 6074 - 모범답안

# n=input()
# n=ord(n)
# v=ord('a')

# while v<=n:
#     print(v)
#     v+=1

    # 등호는 입력받은 값까지 출력해야 하므로 붙인 것이다.
    # 부등식을 이용한 조건들도 상기시켜야 한다.

# 6075

# n=int(input())
# v=0

# while v<=n:
#     print(v)
#     v+=1

# 6076 (6075랑 같은 문제 그러나 다른 방식)

# n=int(input())

# for i in range(n+1):
#     print(i)

# 6077 ★★

# n=int(input())
# sum=0

# for i in range(0,n+1,2):
#     sum+=i
# print(sum)

# sum=0으로 초기화를 해주어야 한다. 선언하지 않은 변수를 if문에서 사용 시 예외가 발생한다.
# 꼭 입력해준 값까지 포함하려면 +1을 해주자. range는 -1을 하기 때문이다.
# print(sum)을 for문 밖에 작성해야 한다. for문 안에 작성 시 계속 반복되어 출력하므로 의도와 다른 값이 출력된다. 

# 6078

# q=ord('q')

# while True:
#     s=input()
#     s=ord(s)
#     if s!=q:
#         print(chr(s))
#     else:
#         print('q')
#         break

# 6078-2

# while True:
#     s=input()
#     if s!='q':
#         print(s)
#     else:
#         print('q')
#         break

# break문을 꼭 넣어서 while True 무한반복문을 탈출하자
# 굳이 ord로 문자를 정수로 형변환하지 않아도 
# 문자로 연산(같다)의 기능은 사용할 수 있다. if s==q:

# 6078 - 모범답안

# while True:
#      x=input()
#      print(x)
#      if x=='q':
#           break

# else문을 이용하지 않고 if-break문만을 이용하여 간결하게 표현하자.

# 6079 ★

# x=int(input())
# n=0
# sum=0

# while True:
#     sum+=n
#     if sum>=x:
#         print(n)
#         break
#     n+=1

# ★★
# 의도와 다른 출력값이 나온다면 흐름을 따라가며 무엇이 잘못됫는지 인지해보자.
# 위 코드에선 if sum<=x: 가 잘못되었다는 점을 알았다. 당연히 처음 sum값은 x값보다 작으므로 if문이 실행될 수 밖에 없다.

# n+=1을 if문 위로 올릴 시 55를 입력하면 11이라는 잘못된 값이 출력된다.
# 이는 코드의 흐름을 복기해보면 출력되기도 전에 n+=1로 인해 +1이 되어서 출력되므로 잘못된 값이 출력된 것이다.
    
# 6080

# m,n=input().split()
# m,n=int(m),int(n)


# for i in range(1,m+1):  (1,3) -> (1,
#     for j in range(1,n+1):   (1,5) -> (1,1),(1,2)(1,3)(1,4)()
#         print(i,j)

# 6081

# x=int(input(),16)

# for j in range(1,16):
#     print('%X*%X=%X'%(x,j,x*j))


# 어떻게 해야 문자를 16진수로 인식하게 할까?
# 이에 대한 답은 어떻게 해야 16진수로 입룍받을까? 인데
# 이는 쉽세 int(,16)처럼 int형변환 인자 뒤에 16을 추가해주면 된다.
# 또한 % 대응법을 잘 알아두도록 하자. % 대응시켜야 하는 개수만큼 %(,,,..)인자 개수를 맞춰주자.

# 6082

# n=int(input())

# for i in range(1,n+1):
#     if i%10==3:
#         print('X', end=' ')
#     elif i%10==6:
#         print('X', end=' ')
#     elif i%10==9:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')


# 반복문과 조건문
# range는 수를 나열할 때(연속으로, 규칙적으로(홀짝수, 등차수열 등)) 많이 사용하는 점을 알아두자.
# elif문 처럼 if문을 적용시키면서 또다른 조건을 만들고 싶을 때 적용되는 변수가 하나이면 사용하기 좋은 것 같다.

# 6082-모범답안

# n = int(input())

# for i in range(1, n+1) :
#   if i%10==3 or i%10==6 or i%10==9 :
#     print("X", end=' ')
#   else :
#     print(i, end=' ')

# or연산을 활용해 조건문의 조건을 깔끔하게 정리했다.\

# 6083★★★ 비트연산필요한듯  6980과 비교 

# r,g,b=input().split()
# r,g,b=int(r),int(g),int(b)

# for i in range(0,r+1):
#     for j in range(0,g+1):
#         for k in range(0,b+1):
#             print(i,j,k)

# 6086

# n=int(input())
# sum=0
# j=0
# while True:
#     sum+=j
#     j+=1
#     if sum>=n:
#         print(sum)
#         break


# for i in range(1):  # range문을 이용하려다 1부터 무한정 더해나가야하는게 필요하므로 while-break문을 사용!
#     sum+=i
#     if sum>=n:
#         print(sum)


# 6087

# n=int(input())

# for i in range(1,n+1):
#     if i%3!=0:
#         print(i,end=' ')
#     else:
#         print('',end='')

# continue문을 사용해서 print('',end='') 대신 넣는 것이 깔끔하다.

# else문 조건(i가 3으로 나눠지면)을 충족하면 conntinue문을 통해 다시 위로 올라가서 반복문을 진행하는 것이다.

# 따라서 continue문을 올바르게 사용하기 위해선
# 모범답안 (else문 사용안하여 더 깔끔)

# n=int(input())

# for i in range(1, n+1) : 
#   if i%3==0 : 
#     continue            # 다음 반복(for문) 단계로 넘어간다 
# print(i, end=' ')       # 밑에 print문은 애초에 for문 바깥에 있기 때문에 진행 X.\

# 6088

# 등차수열 일반항 a(초항)+(n(구하고자 하는 번째)-1)d(공차)
# a,d,n=input().split()
# a,d,n=int(a),int(d),int(n)
# print('%d'%(a+(n-1)*d))  # % 대응없이 바로 a+(n-1)d 해도 무방

# 6089

# a,r,n=input().split()
# a,r,n=int(a),int(r),int(n)
# x=a*r**(n-1)
# print(x)

# 등비수열의 일반항 = a(초항)*r(공비의)**(n-1)(구하고자 하는 번째-1 거듭제곱)

# 6090 ★★(틀린 문제)

# a,m,d,n=input().split()
# a,m,d,n=int(a),int(m),int(d),int(n)
# if m!=1:
#     an=((m**(n-1)*a))+(((m**(n-1))-1)/(m-1))*d
#     print(int(an))
# else:
#     print(a+(n-1)*d)

# 6090은 일반항을 구하라는 문제인줄 알았으나.. 파이썬은 컴퓨터!라는 점을 이용하자.
# 굳이 일반항을 구할 필요가 없다는 뜻이다.
# range()를 이용하면 쉽게 일반항을 구할 수 있다.

# 6090 - 모범답안

# a,m,d,n=input().split()
# a,m,d,n=int(a),int(m),int(d),int(n)

# for i in range(1,n):
#     a=a*m+d

# print(a)

# 6091

# x,y,z=input().split()
# x,y,z=int(x),int(y),int(z)
# day=0

# while True:
#     day+=1
#     if day%x==0 and day%y==0 and day%z==0:
#         print(day)
#         break

# 사고의 흐름
# day= 0에서 머무르면 안되기 때문에 0부터 무한정의 수(물론 만족하는 값을 찾으면 break)가 필요하다.
# 그러므로 while True문을 사용한다.
# 만족하는 조건은 if문을 통해 작성
# 조건 중 and or 연산을 잘 활용하자.

# 6092

n=input() # 번호부른 횟수
s=input() # 몇 번을 불렀는지
# 출력되게할 값은 1번부터 23번까지 자신이 몇번 불렸는지








