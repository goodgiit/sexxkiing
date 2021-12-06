# Chapter03-05

# 파이썬 딕셔너리

# 사전(Dictionary)형은 가장 많이 쓰는 기초형 (Json형태)

# 딕서녀리 자료형(순서X, 키 중복X, 수정O, 삭제O)



# 선언

a={'name' : 'Kim', 'phone': '01033337777', 'birth' : '870514'}

# 소괄호()는 튜플형 중괄호{}는 딕셔너리형  대괄호[]는 리스트형

# 딕셔너리형은  키='name', 'phone', 'birth' 밸류 값 = 'Kim', '01033337777', '870514'으로 이루어져있다.

b={0: 'Hello Python'} # 참고로 어떤 자료형도 키가 될 수있다. 보통은 문자형으로 많이 쓴다

# 소괄호()는 튜플형 중괄호{}는 딕셔너리형  대괄호[]는 리스트형

# 키 중복이란 a={'name' : 'Kim', 'name' : 'Lee'} 처럼 key는 'name' 인데 사전처럼 찾고자하는 단어에 두 가지 뜻이 없는 것처럼 딕셔너리형은 키 중복이 불가능하다.

c={'arr' : [1, 2, 3, 4]}

# 딕셔너리형에서 키만 존재한다면 뒤 밸류 값은 어떠한 자료형이 와도 상관없다.

d={

    'Name' : 'Niceman',

    'City' : 'Seoul',

    'Age' : 33,

    'Grade' : 'A',

    'Status' : True
}

# 내용이 많을 때는 들여쓰기로 가독성이 좋게 한다. 여기서 콤마를 안찍게 되면 오류가 발생한다.

e=dict([

    ('Name', 'Niceman'),

    ('City', 'Seoul'),

    ('Age',  33),

    ('Grade', 'A'),

    ('Status', True)

])

# 딕셔너리형의 표준형이다. dict()안에 리스트형의 튜플형을 선언해야한다. [()] 튜플형에서는 : 이아닌 ,로 수정하면 d와 e는 같은 변수이다.

f=dict(

     Name = 'Nicman',

     City = 'Seoul',

     Age=33,

     Grade='A',

     Status=True

)

# d 변수선언보단 f가 더 쉬울 수 있다.

# 구조적인 딕셔너리형 f를 한 학생의 정보라 생각해보자. 그러한 학생이 100명이 있다고 생각할 때 리스트형으로 a=[f1, f2, f3, f4...] 으로 효율적으로 정보를 저장 관리가 가능하다.

# 출력

print('a = ', type(a), a)

print('a = ', type(b), b)

print('a = ', type(c), c)

print('a = ', type(d), d)

print('a = ', type(e), e)

print('a = ', type(f), f)

# 선언 방법에 있어 d e f는 달랐지만 출력된 결과는 같다는 것을 보여주고 있다.

print()

# 내가 원하는 키로 출력

print('a = ', a['name'])  # 키 존재 X - 에러발생 (속성 attribute로 접근)

# 딕셔너리형에서 인덱스로 접근할 때 키를 사용한다.

print('a = ', a.get('name')) # get 함수 또한 인덱스에 접근할 때 사용한다. 키 존재 X  - None 처리

# print('a = ', a['name'])에서의 출력결과와 같지만 큰 차이점은

# print('a = ', a['name1'])이라고 출력 시 Keyerror가 발생한다, 하지만 get함수를 이용해서 print('a = ', a.get['name1'])이라고 출력 시 'name1'이라는 Key가 없음에도 실행이 되며 None이라는 결과값을 갖고와 더 안정적으로 운용이 가능하다. 따라서 get함수를 많이 사용한다.

print('b = ', b[0])

print('b = ', b.get(0))

print('f = ', f.get('City'))

print('f = ', f.get('Age'))

# 딕셔너라 추가

a['address']='seoul'

print('a = ', a)

# a 딕셔너리에 kry가 address이고 밸류 값이 seoul인 행 추가

# a['name']='seoul'

# 하지만 같은 key인 name에 밸류값 seoul을 추가하려고 하면 원래 name의 밸류 값인 Kim 대신 seoul로 수정이 된다.

a['rank']=[1, 2, 3]

print('a = ', a)

# 물론 리스트형도 추가가 가능하다.

# 딕셔너리 추가

print('a = ', len(a))

print('a = ', len(b))

print('a = ', len(c))

print('a = ', len(d))

# 딕셔너리형도 시퀀스이기 때문에 길이를 확인할 수 있는 함수 len을 이용할 수 있다. 딕셔너리형의 길이는 key의 갯수와 같다. len(a)을 예로 들면 name, phone, birth, address, rank 모두 5개이다.

# 딕셔너리형 함수 (주로 반복문을 사용하기 위해)

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a = ', a.keys())

# key함수는 밸류 값이 아닌 key만을 가져오는 함수이다 위는 a 딕셔너리의 key를 갖고오는 함수이다.

print('b = ', b.keys())

print('c = ', c.keys())

print('d = ', d.keys())

print('a = ', list(a.keys()))

print('a = ', list(a.keys()))

# 여기서 리스트 형변환을 하면 dict_keys 값이 빠지고 오로지 key들을 리스트형태로 출력할 수 있다. 많은 key들이 있어도 리스트형변환을 통해 편하게 key들을 파악할 수 있다.

print('a = ', a.values())

print('b = ', b.values())

print('c = ', c.values())

# values 함수는 밸류 값만을 가져오는 함수이다.

print('a = ', list(a.values()))

print('a = ', list(b.values()))

# 물론 밸류 값들도 리스트 형변환을 통해 밸류값들을 쉽게 파악할 수 있다.

print()



print('a = ', a.items())

print('b = ', b.items())

print('c = ', c.items())

# items 함수를 이용하여 key와 밸류 값 동시에 출력이 가능하다. 출력 형태는 키와 각 밸류 값이 큰리스트형 안(대괄호[])에 하나의 튜플형(소괄호())들로 구성되어 출력된다. 이는 e 딕셔너리를 선언한 방법과 동일한 방식으로 출력되는 것이다.

print('a = ', list(a.items()))

print('b = ', list(b.items()))

print('c = ', list(c.items()))

# 이는 e 딕셔너리를 선언한 방법과 동일한 방식으로 출력되는 것이다. 하나의 큰 리스트형 안에 각 키와 밸류값들이 한 쌍으로 묶여 튜플형으로 구성되는 것,

print()

print('a = ', a.pop('name'))

print('a = ', a)

# pop함수는 꺼내온다음 제거하는 기능을 가진 함수이다. a.pop('name')에서 name 키를 가져오고 print('a = ', a)에서 보면 name을 제거시켰다. name에 해당하는 밸류값 Kim도 제거

print('c = ', c.pop('arr'))

print('c = ', c)

#  c.pop('arr')에서 arr에 해당하는 밸류 값 [1, 2, 3, 4]를 가져오고 print('c = ', c)에서 보면 하나뿐인 key arr이 제거되어 빈 딕셔너리만 출력되었다.

print()

print('f = ', f.popitem())

print('f = ', f)

# popitem함수는 딕셔너리의 임의의 key와 그에 해당하는 밸류 값 하나를 가져오고 제거하는 기능을 가진 함수이다.  위에서는 f 딕셔너리의 아무 key와 그에 해당하는 밸류 값을 가져와 제거하는 기능을 하고 있다.

print('f = ', f.popitem())

print('f = ', f)

# 계속해서 popitem 함수를 이용하면 하나씩 key와 그에 해당하는 밸류 값이 줄어들어 빈 덕셔너리가 된다.

print('f = ', f.popitem())

print('f = ', f)

print('f = ', f.popitem())

print('f = ', f)

print('f = ', f.popitem())

print('f = ', f)

print()

# in 연산자

print('a = ', 'birth' in a)

# in 연산자를 이용해 딕셔너리 안에 해당 key가 있는지 알 수있다. 위에서는 'birth'라는 key가 a 딕셔너리에 있는지 파악하는 기능을 하고 있다. 있으면 True, 없으면 False

print('d = ', 'city' in d)

# 수정

a['test']='test_dict'

print('a = ', a)

# a[]를 통해 a딕셔너리에 추가하고 있다.

a['address']='dj'

print('a = ', a)

# a 딕셔너리에 이미 존재하고 있는 key인 address에 또다른 밸류 값을 넣으면서 기존의 밸류 값을 수정하고 있다.

a.update(birth='990219')

print('a = ', a)

# 하지만 위의 수정방식 보단 update함수를 이용하여 밸류값을 수정할 수 있다. a.update(birth='990219')는 a 딕셔너리의 birth라는 key에 해당하는 밸류 값을 990219로 수정하는 기능을 하고 있다.

temp={'addresss' : 'Busan'}

a.update(temp)

# 아니면 명시적으로 수정방식 temp={'addresss' : 'Busan'} a.update(temp) 을 이용해도 된다,

print('a = ', a)
