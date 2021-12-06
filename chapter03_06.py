# Chapter03-6

# 집합(Set) 특징

# 집합(Set) 자료형 (순서 X, 중복X)

# 많은 데이터를 집합 형태로 저장



# set형 선언

a=set()

b=set([1, 2, 3, 4])

# ()안에 리스트형을 넣어주는 것이 일반적인 set형

c=set([1, 4, 5, 6])

d=set([1, 2, 'Pen', 'Cap', 'Plate'])

# 물론 다른 자료형들이 들어갈 수 있다.

e={'foo', 'bar', 'baz', 'foo', 'qux'}

# 중괄호 또한 이용할 수 있다. 여기서 딕셔너리형은 키와 밸류값(ex - 'name' : 'Kim')이 들어가야 하지만 set형은 위의 형태처럼 들어가면 가능하다.

f={42, 'foo', (1, 2, 3), 3.14159}

# 이렇게 중괄호 내에 정수형 실수형 문자형 튜플형 각기 다른 자료형이 들어갈 수 있다.

# 출력

print('a = ', type(a), a)

print('b = ', type(b), b)

print('c = ', type(c), c)

print('d = ', type(d), d)

# set형은 중복된 데이터는 표시하지 않는다. d 집합의 'foo'라는 원소가 2개 있으나 출력 결과는 하나의 'foo'만 출력된다.

print('e = ', type(e), e)

print('f = ', type(f), f)

# in연산자도 set형에서 가능하다. 딕셔너리형 튜플형 리스트형에서 사용가능한 것들은 모두 사용이 가능하다.

print('a = ', 2 in b)

print()

# 튜플 변환(set -> tuple)

t=tuple(b)

print('t = ', type(t), t)

# 원래는 b=([1, 2, 3, 4]) 집합형이었으나 t=tuple(b)의 튜플형변환으로 인해 t=(1, 2, 3, 4) 튜플형이 되었다.

print('t = ', t[0], t[1:3])

print()

# 튜플형변환을통해 슬라이싱처리를 할 수 있다.

# 리스트 변환(set -> list)

l=list(c)

l2=list(e)

print('l = ', l)

print('l2 =', l2)

# c와 e집합형을 리스트형으로 형변환 하였다.

# 길이

print(len(a))

# 길이가 0인 것은 공집합

print(len(b))

print(len(c))

print(len(d))

print(len(e))

print(len(f))

print()

# 집합의 길이는 원소의 갯수

# 집합 자료형 활용

s1=set([1, 2, 3, 4, 5, 6])

s2= set([4, 5, 6, 7, 8, 9])

print('s1 &s2= ', s1&s2)

# &연산자를 통해 교집합을 찾을 수 있다. 위는 s1&s2의 교집합을 찾는 기능을 하고 있다.

print('s1 &s2 : ', s1.intersection(s2))

# intersection함수를 통해 교집합을 찾을 수 있다. s1집합과 s2집합의 교집합을 찾는 기능을 하고 있다.

print('s1 &s2= ', s1&s2)

print('s1 | s2 : ', s1.union(s2))

# | (shift + 엔터위에 키)연산자를 이용하여 합집합을 찾을 수 있다. 또한 union함수를 이용하여도 합집합을 찾을 수 있다. 위는 s1집합과 s2집합의 합집합을 찾는 기능을 하고 있다.

print('s1 - s2= ', s1-s2)

print('s1 - s2= ', s1.difference(s2))

# - 연산자와 difference함수를 이용해 차집합을 구할 수 있다. 위는 s1집합과 s2집합의 차집합을 찾는 기능을 하고 있다.

# 집합형의 함수

print('s1 & s2 : ', s1.isdisjoint(s2))

# isdisjoint 함수를 이용해 두 집합사이에 공통되는 원소가 있는지 알 수 있다. 여기서 False가 나와야 공통되는 값이 있고 True의 값이 나와야 공통되는 값이 없다는 점을 유의하자.

print('subset : ', s1.issubset(s2))

# issubset 함수를 이용해 두 집합 간 부분 집합 관계를 알 수 있다. 위는 s1이 s2의 부분집합인지를 파악하는 기능을 하고 있다. True = 부분집합 False = 부분집합이 아니다.

print('superset : ', s1.issuperset(s2))

# issuperset s1집합이 s2 집합을 포함하는 지를 파악하는 기능을 하고 있다. 이 점을 통해 issubset 과 issuperset 함수는 서로 상반된 기능을 하고 있는 함수이다.

# 추가 & 제거

s1=set([1, 2, 3, 4])

s1.add(5)

print('s1 :  ', s1)

# add 메소드를 이용해 원소를 추가할 수 있다. 위는 s1집합에 5라는 원소를 추가하는 기능을 하고 있다

s1.remove(2)

# remove 메소드를 이용해 원소를 제거할 수 있다. 위는 s1집합에 2라는 원소를 제거하는 기능을 하고 있다. 기존에 없는 원소를 삭제하려고 하면 에러가 발생한다.

s1.discard(3)

# 또한 discard 메소드를 이용해 원소를 제거할 수 있다. 위는 s1집합에 3이라는 원소를 제거하는 기능을 하고 있다. 여기서 remove메소드 와의 차이점은 remove 메소드는 기존에 없는 원소를 제거하면 에러가 발생하지만 discard 메소드를 통해 기존에 없는 원소를 제거하면 에러(예외)가 발생하지 않는다.

s1.clear()

print('s1 : ', s1)

# clear메소드를 이용해 원소를 한꺼번에 모두 제거할 수 있다. 위는 s1집합의 원소를 모두 제거하는 기능을 하고 있다.

a1=[1, 2, 3, 4]
a1.clear()
print(a1)
# 리스트형도 clear 메소드를 이용해 원소 모두 삭제 가능.
