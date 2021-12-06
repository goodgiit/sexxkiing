
# 2557

# print('Hello World!')

# 1000

# A,B=input().split()
# A,B=int(A),int(B)
# print(A+B)

# 10998

# A,B=input().split()
# A,B=int(A),int(B)
# print(A*B)

# 1001

# A,B=input().split()
# A,B=int(A),int(B)
# print(A-B)

# 1008

# A,B=input().split()
# A,B=int(A),int(B)
# print(A/B)

# 10869

# A,B=map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

# 10430

# A,B,C=map(int,input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

# 괄호를 잘 쳤는 지는 필수점검요소이다.
# 또한 결과값을 통해 41행과 42행은 같지 않고 43행과 44행 또한 같지않다.

# 2558

# A=int(input())
# B=int(input())
# print(A+B)

# 2588

# a=int(input())
# b=input()
# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))

# 어떻게 해야 입력한 숫자들을 자릿수마다 분리할 수 있을까
# 이 문제는 입력하는 문자를 int형으로 먼저 바꾸어주면
# int형은 str형처럼 슬라이싱으로 나누어 줄 수 없기 때문에 문제가 발생한다
# 따라서 그냥 str형으로 입력받은 다음 슬라이싱 후 형 변환을 거쳐 문제를 해결했다.

# 3046

# R1,S=map(int,input().split())
# R2=2*S-R1
# print(R2)

# S=(R1+R2)/2
# 2S=R1+R2
# R2=2S-R1

# 2163(틀린 문제)

# M,N=map(int,input().split())
# print(N*M-1)

# 어떻게 해야 M,N이 1이 될때까지 하나씩 뺀 횟수를 알 수 있을까
# 포인트는 규칙(수학적 접근)을 찾는거인듯 하다.
# 예를 들어 3X3의 사각형을 1X1의 사각형 9조각으로 만들기 위해서
# 먼저 사각형을 2번 자르면 1X3의 사각형 3개를 만들고 (즉 M-1번 자르면 M=1이 될 수 있다.)
# 1X3 사각형 하나를 1X1 사각형으로 만들기 위해선 2번 잘라야 한다.
# 즉 (1X1이 되기 위해선 M-1번 자른  M개의 사각형들 중 하나를 N-1잘라야(위 논리와 비슷) 하기 때문에..  )
# 최종 공식은 M-1+M(N-1)=MN-1이다.

# 11021★

# T=int(input())

# for i in range(T):
#     A,B=map(int,input().split())
#     print('Case #{}: {}'.format(i+1,A+B))

# 반복문 안의 입력문 형태
# print문 format 대응법
# 문제를 잘 읽도록

# 11022

# T=int(input())

# for x in range(1,T+1):
#     A,B=map(int,input().split())
#     print('Case #%d: %d + %d = %d'%(x,A,B,A+B))

# 11021과 같은 문제
# print문의 % 대응법

# 10699

# import time

# print(time.strftime('%Y-%m-%d'))
# print(time.localtime())

# 일반적인 년도-월-날짜 표현
# 순서 바뀌면 출력 순서도 바뀐다.
# 원시적 time 출력은 localtime을 이용하자.

# 1094??/

# X=int(input())
# x=64

# if X<=x:
#     x=x/2

# 1152

# x=input()
# word_count=0
# for i in range(1,len(x)-1):
#     if x[0]==' ' or x[len(x)-1]==' ':
#         word_count+=0
#     if x[i]==' ':
#         word_count+=1
# print(word_count)


# 왜 x[len(x)]로 마지막 문자열을 출력하려면 예외가 발생할까?
# 이는 []에 초점을 맞추면 리스트의 index는 0부터 시작한다.
# 즉 마지막 index번호는 -1을 해주어야 마지막 문자열이 출력가능하다는 사실.



# 공백의 개수를 셀 수 있나?

# 1152 - 모범답안 아주쉬운문제

# print(len(input().split()))

# 문제를 잘 읽어보도록 하자.
# 입력 란에 단어는 공백 한 개로 구분되며, ★★
# 여기서 split()과 len()을 사용할 생각을 했더라면..
# 공백이 연속해서 나오는 경우는 없다.
# 또한 문자열은 공백으로 시작하거나 끝날 수 있다.

# 7287

# print('64')
# print('pkk990219')

# 2525 ★

# A,B=map(int, input().split())
# C=int(input())
# D=B+C
# if (B+C)>=60:
#     A+=(B+C)//60
#     D=D%60
#     if A>=24:
#         A=A%24
#         print(A,D)
#     else:
#         print(A,D)
# else:
#     print(A,D)

# 코드가 내 의도와 다르게 출력되면 천천히 복기하면서 문제를 찾아보자
# 위는 B+C에 대한 코드를 기입하지 않아 계속해서 B+C 그대로의 값이 출력되었다.
# 몫과 나머지 분별 잘하기
# 출력값을 보고 어떤 코드가 틀렸는지 판단하기!
# 위 코드는 A+=(B+C)%60으로 해 B=48 C=25일 시 D=73를 60으로 나눈 나머지는 13으로
# 이를 A에 더하면 의도와 다르게 13을 더하게 된다.
# 또한 D를 선언하는 대신 B+C 그대로 사용하면 예외가 발생한다.

# 2530

# A,B,C=map(int,input().split())
# D=int(input())
# E=C+D

# if E>=60:
#     B+=E//60
#     E=E%60
#     if B>=60:
#         A+=B//60
#         B=B%60
#         if A>=24:
#             A%=24
#             print(A,B,E)
#         else:
#             print(A,B,E)
#     else:
#         print(A,B,E)
# else:
#     print(A,B,E)

# if문 개수에 맞춰 else문도 같게 기입해줘야하는 것 같다.

# 2530 숏코딩

# h,m,s=map(int,input().split())
# a=int(input())
# s+=a
# m+=s//60
# h+=m//60
# print(h%24,m%60,s%60)

# 너무 if문에 사로잡힐 필요 없다.
# 애초에 60미만의 수여도 60으로 나눈 몫은 0이므로 다음 수(m)d에
# 영향을 끼치지 않으므로 위 코드대로 변수 설정 가능
# 더한 수가 60이나 24를 넘어 영향을 끼친다 하더라도 출력문에서 %로 해결

# 2914

# A,I=map(int,input().split())
# A*I

# if A==1:
#     print(A*I)
# else:
#     print(A*(I-1)+1)

# 올림,내림구현을 위하선  math 모듈 사용 후
# math.ceil(올림하고자 하는 수)
# math.floor(내림 하고자 하는 수)
# 이 역시 입출력값을 통해 코드를 구현했다.

# 5355 ★ (화성 수학)

# T=int(input())

# for _ in range(T): # 각 테스트 개수
#     case=list(input().split()) # 입력받은 것들을 공백 기준으로 입력 후
#     answer=0
#     for j in range(len(case)):
#         if j==0:
#             answer+=float(case[j])
#         else:
#             if case[j]=='@':
#                 answer*=3
#             elif case[j]=='%':
#                 answer+=5
#             elif case[j]=='#':
#                 answer-=7
#     print(format(answer,'.2f'))


# 어떻게 해야 문자를 수로 바꿔 연산을 진행할 수 있을까
# 이는 포인트를 잘못 짚었다.
# 처음 수(실수)에 곱해가며 더해가며 재할당하며 값을 구할 수 있었다.
# 또 어떻게 최대 3개의 입력이 가능하게 하지
# 위에 대한 해답은 range(len(case))로 해결한다.
# 입력값이 (정수) () ().. 뒤 문자가 몇 개 오든 그 길이에 밎게 반복문이 반복되기 때문ㅇ;

# 2675

# case=int(input())

# for _ in range(case):
#     x,old_string=input().split()
#     x=int(x)
#     old_string[0:x]=old_string[0]*x
#     old_string[x:2*x]=old_string[x]*x
#     old_string[2*x:3*x]=old_string[2*x]*x
#     ...
    # 이렇게 하다간 언제 끝맺음을 낼지,,?

    # 철자가 달라질때마다 반복해주어야 하는데 어떻게..?

# case=int(input())

# for _ in range(case):
#     x,old=input().split()
#     x=int(x)
#     old=list(old)
#     new=''
#     for i in range(len(old)):
#         old[i]*=x
#         new+=old[i]
#     print(new)

#  일단 입력받은 값들의 용도가 다르기 때문에 자료형을 따로 정리하였다.
# 문자열의 길이만큼 반복한 이유는 문자열의 각 단어마다 입력한 정수만큼 곱해 출력해야 하기 때문이다.
# 문자열의 각 단어마다는 index표현으로 해결
# 하지만 발생한 문제는 리스트형 그대로 출력하면 []안에 각 정수만큼 곱해진 단어가 각각의 원소로 출력되었다.
# 이를 해결하기 위해 new변수에 빈 문자열을 선언해 리스트형과 더했더니 문자열로 출력되었다..왜?

# 2935

# A=int(input())
# B=input()
# C=int(input())

# if B=='+':
#     print(A+C)
# else:
#     print(A*C)

# 9498

# score=int(input())
# if score>=90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>=60:
#     print('D')
# else:
#     print('F')

# 10871




# 11653

# N=int(input())
# i=2
# while N!=1:
#     if N%i==0:
#         N=N/i
#         print(i)
#     else:
#         i+=1


# 소수를 어떻게 구현할까?
# 소수는 1과 자기자신만을 약수로 지닌 수


# 입력한 수가 소수인지 구현
# holy=int(input())

# for i in range (1,holy+1):

# 1789

# 서로 다른! N개의 자연수!의 합이 S 자연수 N의 최대값?

# S=int(input())
# sum=0
# answer=0

# for i in range(1,S+1):
#     sum+=i
#     answer+=1
#     if sum>S:
#         print(i-1)
#         break
#     elif sum==S:
#         print(i)
#         break

# 수학적으로 접근해서 풀어보았더니
# 1부터 하나씩 더해나가야 최대 개수로 더할 수 있다는 결론이 나왔다.

# 2753

# Y=int(input())

# if Y%4==0 and Y%100!=0:
#     print(1)
# elif Y%400==0:
#     print(1)
# else:
#     print(0)

# if 조건에서도 or and를 잘 활용하자.

# 10039

# a=0

# for _ in range(5):
#     student=int(input())
#     if student>=40:
#         a+=student
#     else:
#         a+=40
# print(int(a/5))


# 반복문 안에서 입력받을 경우 그 변수들을 다르게 저장하는 방법?
# 값들을 입력받은 다음 그 값들에 대해 조건들이 있다면 이를 어덯게 표현할까
# 이에 대한 해결로  a=0 변수를 선언해 a+=을 이용하였다.
# 전에 푼 문제들의 해결방식을 잘 생각해야 하는 이유가 있다.

# 1934 ★★★

# T=int(input())

# for i in range(T):
#     A,B=map(int,input().split())
#     for j in range(min(A,B),0,-1): # range 표현 다시 정리하기 + 유클리드 호제법 공부
#         if A%j==0 and B%j==0:  # 공약수 표현
#             print(A*B//j)
#             break


            # 어떻게 해야 가장 큰 공약수를 표현할까..
            # int형은 iterable하지 않아.. list형으로 변환불가..

# d=1
# d=list(d)
# print(d)


# 예제까진 문제없으나 공약수가 2개 이상
# ex) 20 30은 2*5으로 나눠야 함
# 표현엔 무리가 있다.
# 즉 최대공약수로 나눠줘야한다는 사실을 깨우칠수 잇다.
# 최대공약수 표현..?


# A와 B를 1부터 계속 곱해나가다 둘이 일치할 시 출력
# 무한으로 출력되는데 어떻게  멈출까

# 포인트가 잘못되었다.
# 일단 무지성으로 두수를 곱한 후 A*B
# 두 수의 공약수로 나눠야 한다.
# 그렇다면 공약수 표현은 어떻게 해야할까

# 최대공약수 표현
# for i in range(min(a,b),0,-1): # -1이 포인트이다.
#     if a%i==0 and b%i==0:
#         print(i)
#         break

    # 위처럼 하면 작은 수부터 시작하므로 반복문에 의해 의도와 다르게 출력된다.
    # 하지만 큰 수 부터 즉 range의 끝 인자를 -1로 한다면..?

# 1934

# T=int(input())

# for i in range(T):
#     A,B=map(int,input().split())
#     for j in range(1,min(A,B),-1):
#         if A%j==0 and B%j==0:
#             print(j)
#             break

# A=12
# B=16

# for i in range(min(A,B),1,-1):
#     if A%i==0 and B%i==0:
#         print(i)
#         break

# 2480

# x,y,z=map(int,input().split())

# if x==y and y==z:
#     print(10000+x*1000)
# elif x==y:
#     print(1000+x*100)
# elif y==z:
#     print(1000+y*100)
# elif x==z:
#     print(1000+x*100)
# else:
#     if x>y:
#         if x>z:
#             print(x*100)
#         else:
#             print(z*100)
#     else:
#         if y>z:
#             print(y*100)
#         else:
#             print(z*100)
    

# 4101

# while True:
#     A,B=map(int,input().split())
#     if A>B:
#         print('Yes')
#     elif A==0 and B==0:
#         break
#     else:
#         print('No')

# 10156

# K,N,M=map(int,input().split())

# if K*N>M:
#     print(K*N-M)
# else:
#     print(0)

# 3009

# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# x3,y3=map(int,input().split())

# ax=[x1,x2,x3]
# ay=[y1,y2,y3]

# x4=0
# y4=0

# 원소가 하나인 것만을 각 리스트에서 출력한 결과가 답

# if ax.count(x1)==1:
#     x4=x1
# if ax.count(x2)==1:
#     x4=x2
# if ax.count(x3)==1:
#     x4=x3
# if ay.count(y1)==1:
#     y4=y1
# if ay.count(y2)==1:
#     y4=y2
# if ay.count(y3)==1:
#     y4=y3

# print(x4,y4)

# elif와 if문의 차이를 알아보도록 하자.
# 내 생각에 elif문은 다중조건문이라 많은 조건문 중에 한 조건을 만족하면 탈출하는 것 같다.
# 그에 반해 다중if문은 별개의 if문들이라
# 한 조건을 만족해 탈출하더라도 밑에 있는 if문들의 조건을 또 다시 만족하면 
# 그 if문을 만족하고 탈출해야한다. 
# 연계의 차이점인 것 같다. elif문은 결국 하나의 if문이고
# 다중 if문은 여러 개의 if문인 것이다 

# 2476

# N=int(input())

# A=0
# B1=0
# B2=0
# B3=0
# C1=0
# C2=0
# C3=0
# C4=0

# for _ in range(N):
#     x,y,z=map(int,input().split())
#     if x==y and y==z:
#         A=10000+1000*x
#     elif x==y and x!=z:
#         B1=1000+100*x
#     elif y==z and x!=y:
#         B2=1000+100*y
#     elif x==z and x!=y:
#         B3=1000+100*x
#     else:
#         if x>y:
#             if x>z:
#                 C=x*100
#             else:
#                 C=z*100
#         else:
#             if y>z:
#                 C=y*100
#             else:
#                 C4=z*100
# print(max(A,B1,B2,B3,C1,C2,C3,C4))

# 2476


# 반복문에 입력되는 N(사람) 수마다 변수를 다르게 적용할순없나..?

N=int(input())
A=list(0 for _ in range(N))

for i in range(N):
    x,y,z=map(int,input().split())
    if x==y and y==z:
        A[i]=10000+x*1000
    elif y==z:
        A[i]=1000+y*100
    elif x==y:
        A[i]=1000+x*100
    elif x==z:
        A[i]=1000+z*100
    elif x!=y!=z:
        A[i]=100*max(x,y,z)
print(max(A))

# 막히는 부분-------
# 어떻게 해야 각 i(N=사람수)별로 A의 대소관계를 구분할까?
# 해결책은 바로 리스트형을 이용해서 리스트의 원소로 넣게해
# i를 index번호로 이용하는 것이다.
# 문제 발생
# 어떻게 해야 입력한 N(사람 수)만큼 리스트의 크기를 정할 수 있을까
# 리스트 크기 정하는 법
# A=list(0 for _ in range(N))

# 2754

# score=input()
# dic_score={

#     'A+': 4.3,  # dic형에서 ,은 필수이다.
#     'A0': 4.0,
#     'A-': 3.7,
#     'B+': 3.3,
#     'B0': 3.0,
#     'B-': 2.7,
#     'C+': 2.3,
#     'C0': 2.0,
#     'C-': 1.7,
#     'D+': 1.3,
#     'D0': 1.0,
#     'D-': 0.7,
#     'F': 0.0
# }

# print(dic_score.get(score))

# Builtin_function_or_method 예외 발생은 []연산자가 지원하지 못하는 값이 들어갔기 때문이고
# 이를 ()로 바꿔주면 간편하게 수정할 수 있다.

# get 메소드의 장점은 인자의 key가 없을 시 None값을 출력
# 하므로 키가 없는 값을 용이하게 파악할 수 있다.

