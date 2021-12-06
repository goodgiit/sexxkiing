#  파일을 쓰고 읽는 작업을 할 수 있다.

# 외부에서 우리가 수집하거나 작성한 다양한 형식의 파일들을 파이썬으로 가져와서 읽을 수 있다.

# Chapter09-1

# 파일 읽기 및 쓰기

# 읽기 모드 : r(read), 쓰기 모드 : w(write), 추가 모드 : a(append) / 텍스트 모드 : t(text), 바이너리 모드 : b(binary)

# 상대 경로('../(상위 폴더로), ./(현재 위치)'), 절대 경로(ex : 'C:\Django\example') 상대 경로는 현재 폴더의 위치부터 따져보지만 절대 경로는 사용자가 어디 있든지 사용자의 저장 장치의 루트(root)경로부터 따진다.

# 절대 경로로 작성해 놓으면 다른 pc에서도 똑같은 구조로 폴더를 만들어 놓았다면 동작을 하겠지만 현재 폴더 기준으로 예를 들어 resource 파일이 존재하는지 확인할 때와같은 경우에는 상대경로가 더 좋다.



# 파일 읽기(Read)

# 예제1

# 파이썬과 외부에 있는 파일을 연결해주는 내부 함수 open

f=open('./resource/it_news.txt', 'r', encoding='UTF-8')


# open(열고 싶은 파일의 위치(상대경로와 절대경로 작성 가능), 사용자가 사용하고 싶은 옵션(r, w, a) 여기서 세부적으로 텍스트를 읽을거면 rt 바이너리로 읽을 거면 rb 식으로 두번째 인자를 작성한다. 참고로 t는 기본값이므로 생략이 가능해 r = rt이다.

# 세번째 인자로는 가져올 파일의 인코딩 값이 오는데 인코딩은 파일의 종류(엑셀, 워드 등)마다 다르다.) 참고로 rt = r과 같이 파이썬은 기본적으로 UTP-8 으로 인코딩을 진행한다.  즉 encoding = 'UTP-8' 생략 가능 (it_news.txt 파일은 UTP-8로 인코딩하기 때문) 이외에도 인코딩의 종류로는 euc-KR, iso-8859등이 있다.

# 참고로 위 예제에선 상대경로('./resource = 현재위치 ./에 있는 resource파일로)로 it_news.txt 파일을 표현했지만 절대경로로 표현하면 C:\python_basic\resource\it_news.txt\이다.

# 즉 './resource/it_news.txt' 파일을 open함수로 연결해 변수 f에 할당한 것이다.

# 속성 확인

print(dir(f))

# 인코딩(종류) 확인

print(f.encoding)

# 파일 이름

print(f.name)

# 모드 확인

print(f.mode)

# 읽기 기능 확인

cts=f.read()

print(cts)

f.close

# 반드시 close 작업이 필요하다.
# 예제 2

# 보통 예제 1의 방식(open함수를 변수 f에 연결)처럼 사용하진 않는다.

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:

    c=f.read()

    print(c)

    print(iter(c))

    print(list(c))



print()

# with를 이용해 alias(사용자가 정하는 별칭)을 줘 편하게 이용할 수 있고 read기능 뿐 아니라 위에 잇는 mode name ...기능도 가능하다.

# with문에선 f.close가 생략가능하다.(파이썬에서는 with문을 모두 실행하고 나올 때는 with에서 사용했던 리소스들 './resource/it_news.txt', 'r', encoding='UTF-8'을 알아서 반환해주기 때문이다.)

# 들여쓰기가 중요한 의미를 가지고 있다.

# print(iter(c))의 출력 결과를 통해 c를 for문 반복문에서 사용가능하다는 것을 알 수 있다.

# print(list(c))의 기능은 it_news.txt의 파일의 텍스트틀을 한 글자 단위로 list형변환이 되었다.



# 예제3

# read() : 전체 읽기, read(10) : 파일의 10바이트만 읽어온다다.(공백  = 1Byte) 즉 ()안 int형(정수)에 맞는 바이트 수만크 읽어온다.

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:

    c=f.read(20)

    print(c)

    c=f.read(20)

    print(c)

    f.seek(0, 0)

    c=f.read(20)

    print(c)

# 위 with문을 통해 사용자가 마지막에 읽었던 곳을 기억하는 기능을 하고있는 커서의 존재를 알 수 있다.

# seek(0, 0)의 기능은 다시 읽는 파일의 처음 부분으로 돌아가는 기능을 한다. seek의 기능에 따라서 다음 20바이트 읽는 부분에선 처음부터 20바이트를 읽는 부분이 나올 것이다.

# 따라서 seek(from(1), to (2))의 두 인자를 조절해서 읽는 파일을 어디서 읽을 지 세밀하게 조절할 수 있다.



# 예제4

# readline : 한 줄 씩 읽기(한 줄 개행이 되기 전까지 )

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:

    line=f.readline()

    print(line)

    line=f.readline()

    print(line)

# 반복할 때마다 한 줄 그 다음 한 줄씩 가져온다. (반복문으로 효율성 상승)



# 예제5

# readlines (★) : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:

    cts=f.readlines()

    print(cts)

    print()

    for c in cts:

        print(c, end='')

# 위 with문 실행 시 줄 단위로(\n으로 구별) 리스트형으로 생성 즉 한 줄 한 줄이 각각 한 리스트의 서로다른 index인 것이다. 줄이 아예 공백인 it_news.txt파일의 6행은 공백 자체(only \n)가 한 index인 것이다.

# 반복문 작업을 통해 다시 원문으로 redo했다.
# cts리스트의 index 번호순대로(죄측부터) 변수 c에 저장 후 아래 하위구문 print(c, end='')실행 또 다음 index번호 원소 c에 저장 하위구문실행....반복..
# 여기서 의문이 들 수 있다. end=''을 통해 줄바꿈을 방지했는데 왜 줄 바꿈이 될까? 그것은 index 자체가 \n을 가지고 있기 때문이다.
# 예를 들어 0번 index = 'Right now gamers can pay just $1 for access to hundreds of titles across PC \n' 이므로 다음 index와의 줄바꿈을 방지해도  줄바꿈이 되는 것이다.

# 파일 쓰기(write)

# 예제1

with open('./resource/contents1.txt', 'w') as f:

    f.write('I love python\n')

# 기존의 있는 파일을 연결(read할 때) open 함수를 사용했다면 사용자가 쓰고자 하여 없는 파일을 가상으로 연결 할 때도 open함수를 사용한다.

# 즉 쓰고자 할 때 open(쓰고자 하는 파일명(존재하지 않으면 새로운 파일명을 작성), 'w') 물론 여기서도 wt = w이다. binary로 쓰고자 할 땐 wb를 두번째 인자에 넣어주면 된다.

# alias를 이용하여 별칭 f를 붙여주었다. 들여쓰기 !

# f.write('작성하고 싶은 내용') \n = 개행이 됬는 지는 위 with문 실행시 content1.txt 파일에서 (비어있는) 2행까지 나오는 것을 확인할 수 있다.

# 참고로 Atom을 관리자 권한으로 실행해야 새로운 파일을 생성하여 그 파일에 쓰는 것이 가능해진다.



# 예제2

with open('./resource/contents1.txt', 'w') as f:

    f.write('I love python2\n')

# 이렇게 같은 파일에 wirte(text) 모드로 다른 내용을 쓰고자 하면 기존 내용(I love python\n)이 없어지고 위 I love python2\n 내용이 출력된다, 그럼 내용을 추가하고 싶을 땐 어떻게 해야 할까

with open('./resource/contents1.txt', 'at') as f:

    f.write('I love python3\n')

# at(append text)모드를 이용해서 파일(content1.txt)의 기존내용에 추가할 수 있다. (기존 내용 뒤에 삽입)



# 예제3

# wirtelines(★) : 리스트 -> 파일 readlines 메소드는 전체를 읽은 후 라인 단위로 index하나로  리스트형으로 저정하는 것이었다. writelines는 이와 반대로 리스트형으로 되어 있는 것들을 파일로 작성이 가능하게 해준다.

with open('./resource/contents2.txt', 'w') as f:

    list=['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']

    f.writelines(list)

# 이스케이프 문자 \n을 통해 각 index간 개행이 되도록 한다.



# 예제4

with open('./resource/contents3.txt', 'w') as f:

    print('Test Txt Write!', file=f)

    print('Test Txt Write!', file=f)

    print('Test Txt Write!', file=f)

# print문을 통해 파일에 내용을 작성할 수 있다.(print(작성하고자 하는 내용, file=f 여기서 f는 with문 alias로 설정한 f)

# 실행 시 실행되는 파일에 print문이 출력(디버깅)되진 않고 wirte하고자 하는 새로 생성된 파일에 작성이 된다.

# 보통 print문은 사용자가 점검용도로 사용하는 데 콘소레 print문이 많을 시 내용이 잘 안보이므로 file옵션을 이용해 새로운 파일에 내용을 쉡게 볼 수 있다.
