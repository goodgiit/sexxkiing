# 파이썬 인터프리터가 자주 사용되는 함수를 이미 기본값으로 가지고 있다. 이를 내장 함수(Built-in-Function)라 한다.

# Chapter08-1

# 파이썬 내장(Buillt-in) 함수

# 자주 사용하는 함수 위주로 실습

# 사용하다보면 자연스럽게 숙달

# str(), int(), tuple() 형변환은 이미 학습

# abs() : 절대값

print(abs(-3))

# all, any : iterable 요소 검사(참, 거짓)

print(all([1, 2, 3]))

# all 함수 내 인자들이 모두 참이어야 true가 나온다. 하나라도 거짓값 (0, 빈 데이터 등)이있다면 false가 나온다. (and 조건)

print(any([1, 2, 0]))

# any함수는 반대로 함수 내에 하나라도 true값이 있다면 true가 나온다. (or 조건) 모두 false값이어야 false값 출력

# iterable 데이터 tuple, set 모두 사용가능하다.'

# chr : 아스키 -> 문자 , ord : 문자 -> 아스키

print(chr(67))

print(ord('C'))



# enumerate ★ : 인덱스 번호 + iterable한 객체 생성

# iterable하다 : 반복 가능한 list, dictionary, tuple, set형

for i, name in enumerate(['abc', 'bcd', 'efg']):

    print(i, name)

# 출력 결과를 살펴보면 (인덱스 번호) (real value data)가 출력된다.

# enumerate 함수는 두 개의 변수가 필요하다 (위에서는 i에는 인덱스 번호를 받았고 name에선 real value data를 받았다.)

# print(i+1)을 통해 몇 번째 value인지도 아는 식으로 활용할 수 있다.

# filter★ : 반복가능한 객체 요소를 (내가 지정한★) 함수 조건에 맞는 값 추출

def conv_pos(x):

    return abs(x) > 2 # return 값은 조건식이므로 true or false값을 반환한다.

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))

# 함수를 호출(conv_pos())가 아닌 함수 자체(conv_pos)를 넣는 것에 유의하자.

# 형변환을 해줘야 올바른 값 출력(안하게 되면 결과값이 object(id 값)으로 나오게 된다.)

# 위 코드 출력 시 conv_pos함수의 반환값 조건 abs(x)>2에맞는 x : -3, -5, 6이 리스트형으로 나오게 된다.

print(list(filter(lambda x: abs(x)>2, [1, -3, 2, 0, -5, 6])))

# lambda 함수를 이용해 간단하게 출력할 수 있다. 위처럼 굳이 함수를 한번 사용할 건데 함수를 위에 선언할 필요성이 없어지게 된 것이다.

# id : 객체의 주소값(레퍼런스) 반환 (주소가 다르면 객체가 다른 것)

print(id(int(5)))

print(id(7))

# len : 데이터의 길이 반환

print(len('abcdefg'))

print(len([1, 2, 3, 4, 5, 6, 7]))

# print(len()-1)을 통해 index 번호를 구한다든지해서 사용할수 있다.

# max, min : 최대값, 최소값

print(max([1, 2, 3]))

print(max('pythonstudy'))

# 문자열의 최대 최소는 abcd순으로 오름차순이기 때문에 pythonstudy에서 제일 큰 값은 y 제일 작은 값은 d가 된다.

print(min([1, 2, 3]))

print(min('pythonstudy'))



# map(★) : 반복가능한 객체 요소를 지정한 함수 실행 후 추출

# filter 함수는 조건식을통해 true인지 false인지 따져 true인 것들만 필터링해주었지만 map함수는 지정한 함수를 거친값들을 모두 함쳐서 반환한다.

def conv_abs(x):

    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))

# map((함수 이름), (함수에 대입하고 싶은 값))

# 이를 통해 map함수는 지정한 함수를 통과시켜 함수가 반환해주는 값을 받는다.

print(list(map(lambda x:abs(x), [1, -3, 2, 0, -5, 6])))

# 물론 람다식으로도 사용가능하다.

print(list(range(1, 10, 2)))

# 1부터 10(-1★)=9까지 2라는 간격을 1->(2생략)->3 (-> 2개) 두는 원소들 생성

print(list(range(0, -15, -1)))

# 0부터 -15(+1★음수일땐 +1임을 유의하자.)= -14까지 -1이라는 간격을 두는(0 -> -1) 원소들 생성

# round : 반올림 함수

print(round(6.5781, 2))

# round(반올림하고자 하는 수, 반올림하고싶은 자릿수) 즉 위 print문은 6.5781을 반올림하고자 하는 자리는 소수 둘째자리 수이기 때문에 그 뒤인 셋째자리에서 반올림되어 6.578 -> 6.58이 된다.

print(round(5.6))

# 위 print문처럼 두번째 인자를 두지 않을 경우에는 첫째자리에서 바로 반올림되어 5.6 -> 6이 된다.



# sorted : 반복가능한 객체(Irterable)정렬 후 반환

print(sorted([6, 7, 4, 3, 1, 2]))

# 6, 7, 4, 3, 1, 2이 오름차순으로 정렬되어 출력된다.

a = sorted([6, 7, 4, 3, 1, 2])

print(a)

# 위 변수 선언과 print문을 통해 반환되었다는 것을 알 수 있다.

print(sorted(['p', 'y', 't', 'h', 'o', 'n']))

# 문자열의 오름차순은 abc 순이다.



# sum : 반복가능한 객체(Iterable) 합 반환

print(sum([6, 7, 8, 9, 10]))

print(sum(range(1, 101)))

# range, sum함수를 이용하여 1부터 100까지의 합을 바로 도출할 수 있다.



# type : 자료형 확인 함수

print(type(3))

print(type({}))

# 여기서 빈 중괄호의 자료형은 dic 형으로 인식하지만 {3,4} 처럼 차있는 데이터는 set형으로 인식한다는 사실!

print(type(()))

print(type([]))



# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환

print(list(zip([10, 20, 30], [40, 50, 60])))

# 이의 결과는 [10, 20, 30], [40, 50, 60] 두 개의 리스트들 중 각 첫번째 원소들을 하나의 튜플로 묶고 (10, 40) 나머지 원소들도 하나의 튜플로 각 번째끼리 묶인다(zip)

# 여기서 리스트형변환을 안하게 되면 zip 오브젝트로 출력되므로 사용자가 원하는 형의 형변환이 필요하다.

print(list(zip([10, 20, 30], [40, 50])))

# 이렇게 짝이 안맞게 되는 경우는 짝이 맞게 되는 번째까지만 적용하고 [(10, 40), (20, 50)] (즉, 각 리스트들의 두번쨰 원소까지만) 짝이 없는 것들은 반환되지 않는다.

print(type(list(zip([10, 20, 30], [40, 50, 60]))[0]))

# zip 함수는 tuple형으로 짝을 만들어서 반환
