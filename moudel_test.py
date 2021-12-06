import sys

print(sys.path)
print(type(sys.path))

# 이런 경우에 type을 많이 사용한다. 현재 sys.path의 type는 리스트형이다.

# 리스트형에 데이터를 추가할 때는 append, insertm index번호로 수정이 가능하다.

# append 메소드를 이용하여 sys.path 즉 모듈 경로에 데이터를 마지막에 하나 추가해 보자

# 모듈 경로 삽입

# sys.path.append('C:/python_moudle')

# 추가 인자는 추가하고자 하는 모듈의 경로(모듈 파일의 위치)(모듈 파일명X)이다.

# sys.append 행은 영구적으로 되는 것이 아니라 이 코드상에서만 실행되는 것이다.

# 실행되는 것을 확인했다면 잠깐 주석처리 수업진행을 위해

# print(sys.path)

# import test_moudle

# 경로에 추가함으로써 test_moudle(모듈)이 검색되는 것을 알 수 있다.

# 이로써 실행시키면 chapter 06_02.py 파일에 있던 print코드가 자동으로 실행이 되었다. 하지만 원래는 이 내용이 실행되면 안 된다. 그 이유는 우리가 사용하기 전에 chapter06_02.py (모듈)의 모든 내용을 불러오기 때문이다.



# 모듈 사용

# print(test_moudle.power(10, 3))

# 모듈 파일명(test_moudle)(.)power(모듈파일 내 있었던 함수)(10, 3)(함수의 두 인자)

# 실행되는 것을 확인했다면 주석 처리 수업진행을 위해

# 모듈 파일 내 print문들이 실행되지 않기 위해서는 어떤 작업이 필요할까? 모듈 파일 내 print문의 수정(제거 또는 주석처리)이 필요하다.

# 파이썬에서는 다른 곳에서 외부적으로 이 파일을 import할 경우(즉, chapter06_02.py 파일 기준이다.)와 자기 자신을 스스로 실행할 경우를 구분하는 예약어 main이 있다.





# chapter 파일들의 상위폴더 pyton_basic은 기본적으로 sys.path 경로에 등록되어 있다. = 외부에서 모듈로서 가져다 쓸 수 있다(impert할 수 있다)는 사실

import chapter06_02

print(chapter06_02.add(10, 100000))

# 이렇게 외부에서 chapter06_02.py 파일 내 함수를 이용할 수 있다.
