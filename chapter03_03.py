# Chapter03-3

# 파이썬 리스트

# 리스트(시퀀스) 순서가 존재 여러가지 데이터 타입을 담을 수 있다.( 배열과 대체해서 사용가능 )

# 자료구조에서 중요

# 리스트 자료형(순서  O, 중복 O, 수정 O, 삭제 O)

# 버스정류장 줄을 서는 상황과 비슷하다.



# 선언

a=[] # 빈 리스트

print(type(a))

b=list() #이 또한 빈 리스트

c=[70,75,80,85] # 70부터 0번 85까지 3번 즉 모두 4개의 원소를 가지고 있는 리스트이다.

print(len(c))

d=[1000, 10000, 'Ace', 'Base', 'Captine']  # 서로 다른 자료형을 한 리스트 안에 담을 수 있다.

e=[1000, 10000, ['Ace', 'Base', 'Captine']]  # 리스트 안에 리스트를 담을 수 있다. 이 때 e 리스트의 2번은 ['Ace', 'Base', 'Captine']가 된다.

f=[21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱(원하는 데이터를 꺼내오는 과정)

print('>>>>>')

print('d = ', type(d), d)

print('d = ', d[1])

# d 리스트의 10000을 가져오고 싶다면 10000의 번호는 1번이므로 d[1]을 삽입

print('d[0]+d[1]+d[1] = ', d[0]+d[1]+d[1])

# d[0]+d[1]+d[1] = 1000+10000+10000=21000 모두 int형

print('d[-1] = ', d[-1])

# str형에서와 마찬가지로 음수는 오른쪽 끝부터 시작 0이아닌 -1임을 유의하자.

print('e[-1][1] = ', e[-1][1])

# e[-1]은 ['Ace', 'Base', 'Captine']으로 리스트이다. 여기서 [1]은 'Base'이다. 따라서 e[-1][1] = Base이다.

print(type(e[-1][1]))

# 이는 문자를 출력하므로 str형이다.

print(list(e[-1][1]))

# 이를 list형으로 형변환하면 ['B' , 'a' , 's' , 'e'] 즉 'B'부터 0번(-4번) e까지 3번(-1번)인 리스트가 출력된다.(문자열도 시퀀스=순서가 있다.)

# 슬라이싱

print('d[0:3] = ', d[0:3])

# d리스트의 0번(1000)부터 3(-1★)=2번('Ace')까지 출력된다.

print('d[2:] = ', d[2:])

# d리스트의 2번('Ace')부터 끝번('Captine')까지 출력

print('e[-1][1:3] = ', e[-1][1:3])

# e[-1] = ['Ace', 'Base', 'Captine'] 리스트에서 [1:3] 즉 1번('Base')부터 3-1=2번('Captine')까지 출력

# 리스트 연산

print('c + d', c+d)  # 리스트 + 리스트 = 리스트 (집합개념) 순서는 순행

print('c * 3', c*3) # 원소개수의 곱 c리스트의 원소는 4개 이를 3에 곱해 12개의 원소가 나오게 됨 순서는 순행

# print("'Test' + c[0]", 'Test' +c[0])

# 문자 'Test'와 c[0]=70(정수)을 더하면 에러발생

print("'Test' + c[0]", 'Test' + str(c[0]))

# 에러없이 더하기 위해서는 c[0]=70을 문자형에 맞게 str형변환
# 값 비교

print(c == c[:3] + c[3:])

# c리스트는 모두 3번까지 있는 4개원소를 가진 리스트이다. 따라서 c[:3](0번부터2번까지)+c[3:](3번부터끝까지)=c이다.

print(c)

print(c[:3] + c[3:])

print()

# Identity(id)

temp = c

print(temp, c)

# c 리스트에 10만개의 원소가 있다 해보자.

print(id(temp))

print(id(c))

# id(temp) = id(c) 같은 아아덴티티 값을 갖고 있다. 파이썬이 문자열과 마찬가지로 쾌적하고 빠른 환경을 위해 변수의 할(복사)시 같은 주소값을 보고 있다.(공유)

# 리스트 수정, 삭제

print(">>>>>")

c[0]=4

print('c = ', c)

# 원래 c[0] 자리는 70이었지만 수정을 통해 c[0]=4가 되었다.

c[1:2]=['a', 'b', 'c']

print('c = ', c)

# 이는 c[1:2] = 75가 ['a', 'b', 'c']라는 리스트로 수정되었다. 여기서 정수 원소를 리스트 원소로 수정한다해도 리스트 안에 리스트로 수정되는 것이 아닌 각 'a' 'b' 'c'라는 문자 원소로 들어가게 된다.

c[1]=['a', 'b', 'c']

print('c = ', c)

# 여기서 c[1:2] 과 c[1]이 같은 자리라 해도 다른 결과가 나오게 된다. 이렇게 실행하게 되면 리스트 안에 리스트로 들어가게 된다. 또한  c[1:2]=[['a', 'b', 'c']] 이렇게 수정하면 리스트 안에 리스트로 들어가게 된다.이를 중첩이라 한다.

c[1:3]=[]

print('c = ', c)

# c[1:3]=[]는 c 리스트의 1번(['a', 'b', 'c']), 2번('b')을 비워라(삭제하라)는 의미. (제거라는 다른 의미)

del c[2]

# del은 제거의 기능 c[2] =80을 제거

print('c = ', c)

print()

# 리스트 함수

a=[5, 2, 3, 1, 4]

print('a = ', a)

# a리스트의 마지막 원소를 추가하고 싶어서 a[5]=10을 선언해서 출력해도 결과는 바뀌지 않는다.

a.append(10)

print('a = ', a)

# append 함수를 이용해 끝부붙에 마지막 원소를 추가하는 기능을 가진 함수이다.

a.sort()

print('a = ', a)

# sort 함수를 이용해 오름차순으로 원소들을 정리할 수 있다.

a.reverse()

print('a = ', a)

# reverse함수를 이용해 역순(내림차순)으로 원소들을 정리할 수 있다.

print('a = ', a.index(3))

# a[3] = a.index[3] 이다. a[3]이 파이썬 내부적으로 a.index[3]으로 처리하는 것.

a.insert(2, 7)

print('a = ', a)

# insert함수는 지금까지는 끝자리에 원소를 추가하는 기능을 가진 append함수와 다르게 기존 원소 사이에 넣는 기능을 가진 함수이다. 위 a.insert(2, 7)은 a 리스트의 2번 자리(4)에 7을 넣는 기능을 하고 있다.(삽입)

a.reverse()

print('a = ', a)

# del a[6]

# 이는 a의 6번(10)을 지우는 기능을 가진 del함수이다. 하지만 이는 a 리스트의 원소가 10만개가 있다고 하면 눈으로 파악하기 힘들다.

a.remove(10)

print('a = ', a)

# 효율적으로 리스트 안에 원소를 제거하기 위해 remove 함수를 활용한다. 제거되길 원하는 원소의 값을 넣으면 제거되는 기능을 가진 함수이다. 위는 a원소 10을 제거하는 기능을 하고있다.

print('a = ', a.pop())

print('a = ', a)

# pop 함수는 기존의 리스트에서 마지막 index에 해당하는 원소를 가져오고 나머지 원소들로 리스트를 구성하는 기능을 가진 함수

# lifo = last in first out 여러 접시들을 깔고 다시 가져가는 상황 = 웹 브라우저의 바로가기, 뒤로가기 등

# fifo = first in first out 가장 처음에 들어오고 처음에 나간다,

print('a = ', a.count(4))

# ★ count함수는 리스트안에 같은 원소의 갯수를 찾는 기능을 가진 함수이다. 위 행에서는 a 리스트 안에 4라는 원소가 몇개 인지를 확인하는 기능을 하고있다. count함수는 리스트의 원소가 많을 때 유용하게 사용가능하다.

ex = [8, 9]

a.extend(ex)

print('a = ', a)

# extend 함수는 위에 슬라이싱 기능을 이용하여 리스트 안에 원소를 추가했던 기능과 같다.

# 삭제 : remove(★), pop(알고리즘), del(데이터 수 적을때)

# 반복문 활용

while a:
    data=a.pop()
    print(data)

# 반복문에서의 pop함수는 끝 부분의 원소부터 시작해 비워가는데 다 비워지면 while문 종료.
