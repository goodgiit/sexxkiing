# Chapter04-3

# 파이썬 반복문

# While 실습



# while 표현법 <expr>:

#    <statment(s)>(들여쓰기 가능, statment=코드작성)

# while문은 if문과 비슷하게 조건을 만족할 때까지 반복한다.

# if, for, while문을 통해 프로그램의 입력과 출력 그런것들을 제어할 수 있다. 이들을 흐름 제어문이라한다.



# 예제1

n=5

while n>0:
    print(n)
    n=n-1



# 여기서 n=n-1 행이 없이 실행하면 무한히 반복되어 다운될 수 있다. 즉 while문은 조건을 만족시키는 동안 계속 반복되기 때문에 조건을 감소시키거나 증가시키는 그런 변화를 일으키는 조건을 while문 내부에 넣어서 사용해야 한다. 또한 while True 여도 무한히 실행된다.

# 예제 2

a=['foo', 'bar', 'baz']

while a:
    print(a.pop())

# print(a) 그대로 실행하면 while a는 a리스트의 원소의 수 3개에 따라 3번 반복이 아니라 무한히 실행되는 것이다. 왜? True = 빈 원소(0)가 아닌 어떤 차있는 원소 이기 때문이다. 따라서 while()에서 ()에 해당하는 곳이 True인지 False인지 파악하도록 하자. 여기서는 pop함수를 이용해 print(a.pop())를 통해 a리스트의 원소를 하나씩 가져와 줄이는 기능을 통해 while a에서 a=0 -> a=False가 되도록 하여 while문이 실행되도록 하고있다. 참고로 a.pop() = a.pop(-1)

# 예제 3 (if 중첩)

# break, continue

n=5

while n>0:
    n-=1
    if n==2:
        break
    print(n)
print('Loop Ended.')

# 순차적으로 n=5이므로 하위구문(n-=1)이 진행되어 n=4가 된다. 그 다음 if n==2:는 만족시키지 못하므로 break(탈출)하지 못하고 print(n)을 통해 출력된다. 이 과정을 한 번더 반복한 후 n=3일때 while의 하위구문이 진행되어 n=2가 되어 if 의 조건문을 만족시켜 break하게 되고 마지막 print('Loop Ended.')이 실행된다.

# break문이 while의 하위구문인 if의 하위구문이므로 while문까지 break하는 것이다.

# 예제4

m=5

while m>0:
    m-=1
    if m==2:
        continue
    print(n)
print('Loop Ended.')

# 위 과정과 비슷한 논리를 거친다. 처음에 m=5이므로 while의 조건을 만족시켜 m-=1을 진행시켜 m=4가 된다. 하지만 if의 조건문(m==2)을 만족시키지 못하므로 if의 하위구문 continue는 실행되지 않고 while의 하위구문2 print(m)을 통해 4가 출력된다. 이 와같은 과정을 한번 더 거친 다음 m=3일 때 while의 하위구문1을 통해 -1감소되어 m=2가 되어 if의 조건문을 만족시켜 continue문이 실행되어 print(m)을 거치지 않고 다시 while문의 조건문으로 이동하여 m=2인상태에서 m=5일 때와 같은 과정이 진행된다. 즉 m=0이 되어 print(m)을 통해 출력되는 과정이 마지막으로 진행되어 출력 결과 4,3,1,0이 출력된다.

# 예제 5

i=1

while i<=10:
    print('i:', i)
    if i==6:
        break
    i+=1

# 거의 바로 위에서 했던 방식과 유사하나 여기서는 증가되는 논리과정을 거치다 i=5일 때 마지막 과정을 거쳐 if=6이 되었을 때 print문을 통해 출력이 된 다음 if문의 조건문을 만족시키므로 if문의 하위구문인 break한다.

# while문은 if문(중첩)과 많이 사용한다.



# 예제6(While-else 구문)

n=10

while n>0:
    n-=1
    print(n)
    if n==5:
        break
else:
    print('else out.')

# 이렇게 실행한다면 else문은 실행되지 않는다. 왜냐하면 if n==5: break 를 통해  while문을 빠져나갔기 때문에 else문은 실행되지 않는다. else문이 실행되기 위해서는 정상적인 모든 반복이 진행되어 야 하므로 if n==5: break문을 제거해야 한다.(마지막에 한 번 실행햐야할 프로그램을 짤 때 유용)(물론 for문도 이와 같다.)

# 예제7

a=['foo', 'bar', 'baz', 'qux']

s='qux'

i=0

while i < len(a): # len(a)=4
    if a[i]==s:  # if a[i]='qux'
        break  # 이는 원하는 값을 찾을 시 break하겠다는 것과 같다.
    i+=1  # 리스트의 원소는 각 번호가 있다는 사실을 유의하자. 'foo'부터 0번에서 'qux' 3번까지 즉 이 흐름 제어문은 a[0]~a[3]까지 a리스트의 원소를 찾아 if a[i]==s:를 통해 qux가 있는지 확인하는 while문이다.
else:
    print(s, 'not found in list.')

# else문은 혹시 내가 찾는 원소가 변수 안에 없을 시 실행되는 값이다.(ex s='Kim')

# 무한반복 (주의!)

# while True:
# print('foo')


# 예제 8

a=['foo', 'bar', 'baz']

while True:  # 이렇게 작성 시 break문이 필수적이다. 없을 시 무한반복이 되기 때문!
    if not a: # a= 빈 리스트가 아닌 원소가 존재하므로 not a=not True=>False이므로 if문의 하위구문이 실행되지 않지만 밑에 pop를 통해 a리스트는 오른쪽 끝 원소를 하나씩 가져와 없어지기 때문에 결국 a리스트는 빈 리스트가 되어 a=False가 되어 if not a= in not False=>if True가 되어 break가 실행되어 while문을 탈출한다.
        break
    print(a.pop())
