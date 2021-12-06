# Chapter08-2

# 파이썬 외장(External) 함수

# 실제 프로그램 개발 중 자주 사용

# 종류 : sys, pickle, shutil, temfile, time, random



# 예제 1

import sys

print(sys.argv)

# 파이썬 파일을 외부에서 실행할 때 파이썬에 어떤 값을 전달해서(함수에서 인자로 넘기듯이) 예를 들어 그 값이 1일 경우에는 1번모드로 2일 경우엔 2번모드로 실행시킬 수 있다.

# 예제2(강제 종료)

# sys.exit()



# 예제 3(파이썬 패키지 위치)

print(sys.path)

# 실행시키면 현재 모든 패키지들의 위치를 출력해준다



# pickle(★) : 객체 파일 쓰기

import pickle

# 모델 등을 사용자의 하드웨어에 저장할 때 즉 텍스트 같은 것들은 텍스트 파일로 작성가능하지만 클래스 클래스 안에서 이루어진 어떤 파이썬의 자료형을 쓸 때 코드를 쓰고 객체 자체를 새로운 파일로 작성 가능

# 파이썬에서 읽을 수 있는 데이터타입(class, list, tuple, dic, set....)을 파일로 쓸 수 있다 또한 읽을 수도 있다..



# 예제4(쓰기)

f=open("test.obj", 'wb')

# open(사용자가 쓰고 싶은 파일명.확장자명은 임의대로 설정 가능, ), (wb = writing binary)

obj={1:'python', 2:'study', 3:'basic'}

# 우리가 쓸 코드 작성 (여기서는 key는 숫자이고 value가 문자형인 dic형)

pickle.dump(obj, f)

# pickle.dump(쓰고자 하는 코드가 담긴 변수,명 쓸 파일을 인자로 담은 open함수를 담은 변수명)

f.close

# 열었으면 꼭 닫아주는 것이 필요하다.

# 실행 시 test.obj라는 파일이 신규생성된다

# 하지만 실행 시 해독불가능한 문자가 쓰여지는데 (확장자명이 .obj)우리가 pickle로 쓴 것들은 파이썬으로  와서(.py) 읽으면 dic형을 읽을 수 있다.(쓰기의 반대)



# 예제5(읽기)

f=open('test.obj', 'rb')

# open(읽고자 하는 파일명, rb = read binary)

# open('c: / test.obj') 처럼 경로를 지정해준다면 지정해준 위치에 파일을 읽고 쓸 수 있다. 경로를 지정하지 않았다면 현재 실행되는 위치에서 쓰고 읽는 것이다.

data = pickle.load(f)

# 쓸 때는 dump 메소드 읽을 때는 load 메소드 load(읽고자 하는 파일이 담긴 변수 (=f))

print(data, type(data))

f.close

# 물론 close 작업도 필수!
# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련

# 운영체제에서 사용할 수 있는 기능을 파이썬 코드로 할 수 있게 지원, 제공(메크로, 카톡실행, 음악재생, 특정 게임실행 등등)

# mkdir(폴더 생성), rmdir(폴더 제거, 비어있으면 삭제), rename(폴더명 재입력)

# 예제 6

import os

print(os.environ)

# 위 print문을 통해 운영체제의 정보를 알 수 있다. dic형으로 출력된다. 파이썬에서 dic형은 아주 증요한 자료형

print(os.environ["USERNAME"])

print(os.environ["ATOM_HOME"])

# dic형으로 출력되므로 key값을 입력하면 그 key에대한 value(값)을 알 수 있다.

# 예제7(현재 경로 출력)

print(os.getcwd())

# 파이썬이 실행되고 있는 파일명(python_basic이 출력되는 것으로 보아 가장 부모파일이 출력) 출력

# time (★) : 시간 관련 처리

import time

# 예제 8

print(time.time())

# 현재 시간을 세밀한단위(밀리세컨드)까지 출력

# 예제 9(예제 8의 출력물을 보기 좋게 형태 변환)

print(time.localtime(time.time()))

# 현재 시간을 년 월 일 ... 단위로 보기 좋게 출력

# 하지만 이 방식을 많이 사용하진 않는다.

# 예제 10(간단하게 표현)

print(time.ctime())

# 예제 9보다 더 간결하고 보기 좋게 출력할 수 있다.

# 예제11(★)(형식 표현)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# strtime = stringformattime 메소드를 통해 사용자가 원하는 형식대로 출력 가능(Y=Year, m=month, d=day, H=Hour, M=Minute) 물론 순서를 바꿔도 그 순서대로 년월일 대로 출력된다.

# strftime(표현하고자 하는 형식, 원시적 형태대로 출력되는 localtime)

# 예제 12(시간 간격을 고의적으로 발생)

for i in range(5): # 0 - 4까지 원소 생성

    print(i)

  #  time.sleep(1)

# time.sleep() 괄호 안엔 초(second)가 들어간다 time.sleep(1)은 1초마다 for문을 한번씩 실행하겠다는 뜻이다.



# random : 난수 리턴

import random

# external function(외장 함수)들은 import문을 통해서 가져와야 한다.

# 예제 13

print(random.random())

# random.random() : 0부터 1사이의 난수 생성 실행할 때마다 다른 수 생성(난수니까)

# 예제14

print(random.randint(1, 45))

# random.randint() : 첫번째 인자와 두번째인자 사의 int(정수)값 랜덤으로 생성

print(random.randrange(1, 45))

# range함수와 같게 -1을 하는것이다. 위 print문에선 1부터45(-1★)=44까지의 정수 랜덤으로 생성

# 예제15(섞기)

d=[1, 2, 3, 4, 5]

random.shuffle(d)

# suffle메소드를 통해 d리스트 원소들의 순서를 무작위로 섞는다,

print(d)

# 실행할 때마다 순서가 달라짐 데이터 분석에서 표본생성을 할 때 많이 사용, 예를 들어 1억개 중 천 개를 뽑고 섞어서 테스트 해보는데 사용할 수 있다.

# 예제16(무작위 선택)

c=random.choice(d)

print(c)

# d리스트의 원소들 중 임의로 하나의 숫자가 뽑혀 출력된다. 물론 실핼할 때마다 달라짐. 반복가능한(Iterable) 데이터형에서 사용가능하다.

# webbrouser : 본인 OS의 웹 브라우저 실행

import webbrowser

webbrowser.open("http://google.com")

# 괄호()에는 접속하고자 하는 URL 주소를 입력하면 된다.

webbrowser.open_new("http://google.com")

# opennew는 새 창으로 열린다. 기존의 탭이 있을 시 탭을 추가해서 열린다.
