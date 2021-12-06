# CSV 파일 : 데이터 과학분야에서 널리 사용, 서로 다른 프로그램에서 데이터를 주고 받을 때 csv 파일형식으로 전달 파이썬은 내부적으로 csv 파일로 쓰거나 읽을 수 있는 패키지 제공

# 콤마(,)로 구분이 되어있는 recod set이다. 어떤 집합을 파일로 저장할 때 csv 파일로 저장하면 사용자가 규칙에 맞게 데이터베이스에 있는 어떤 내용을 csv파일형식으로 변환, 저장하면 또 다른 응용 프로그램에서 많이 사용하기도 한다.

# Chapter09-2

# CSV 파일 읽기 및 쓰기



# CSV : MEME(mymetype) - text/csv (예를 들어 웹브라우저의 MEME는 text/html)

import csv

# test1.csv 파일을 통해 첫번쨰 1행에 헤더를 넣어주는 관습이 있다. 파일을 보면 Name, Code로 되어있는데(해당 csv파일의 양식을 보여준다. 여기서는 국가 이름, 국가 코드) 콤마(,)로 레코드를 구분하고 있다. Code는 국가 코드임을 파일을 보고 알 수 있다.

# test2.csv 파일을 통해 레코드는무조건 콤마(,)로 구분되지 않아도 된다.(공백, ㅣ 등)(하지만 콤마가 정석)

# 예제1

with open('./resource/test1.csv', 'r') as f:

    reader = csv.reader(f)

    next(reader)

# test1.csv 파일은 encoding='UTP-8'이므로 생략해도 실행 가능(파이썬 내부적으로 UTP-8 실행)

    # 객체 확인

    print(reader)

    # 타입 확인

    print(type(reader))

    # 속성 확인 # __iter__ 존재 여부 확인

    print(dir(reader))

 # 속성값을 통해 __iter__ 이 있어 for문에서 사용가능하다는 것을 알 수 있다.

    print()

    for c in reader:

        print(c)

# 위 반복문 실행 시 리스트형으로 csv파일을 읽어온다.(두개의 레코드가 한 리스트에..)

# 맨 위의 리스트가 헤더(양식)로 되어있는 리스트이기 때문에 읽을 필요성이 없다면 next(reader)를 통해 헤더를 스킵할 수 있다. 이 또한 커서의 개념(마지막 끝난 곳을 기억)을 통해 파악할 수 있다.

# next(reader) 중복을 통해 중복된 횟수만큼 스킵이 가능하다.

        print(type(c))

# 위  print문을 통해 list형으로 가져온다는 것을 알 수 있다.

        # list to str

        print(''.join(c))

#  join 메소드를 통해 출력해보면 Name과 Code 두 레코드가 ''(공백)으로 붙은 모습을 알 수 있다. ' '(띄어쓰기) 가 되어있다면 두 레코드가 한 칸 띄어져서 출력된다. 핵심은 리스트형에서 문자형으로 바뀌어 출력되었다는 점이다. 사용자가 보고 싶은 형태로 볼 수 있다,

# 예제2

with open('./resource/test2.csv', 'r') as f:

    reader=csv.reader(f, delimiter='|')

    for c in reader:

        print(c)

# delimiter='|'에서 del은 구분자인데 이 구분자가 없고 예제1번처럼 실행 시 (test2.csv파일은 test1파일과 다르게 ,구분이 아닌 | 으로 되어있다.) | 포람에서 두 레코드를 구분짓지 못하고 하나로 묶어 한 index로 처리해 나와버린다. 여기서 del구분자를 이용해 '|'로 구분하겠다는 것을 명시해주면 두 레코드(Name, Code)를 구분해 두 개의 index를 가진 리스트로 가져오게 된다.

# 예제3 (csv파일을 딕셔너리형으로 출력 가능)

with open('./resource/test1.csv', 'r') as f:

    reader=csv.DictReader(f)

    # 확인

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k,v in c.items():
            print(k, v)
        print('-----------')


#  레코드들로 Key와 Value가 나눠져(Key : 헤더에있는 값들(Name, Code), Value : 헤더에 해당되는 값들 ) 딕셔너리형으로 출력되는 것을 알 수 있다.

# items 는 key와 value값 반환

# 예제4

w=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

# 7개의 index를 가진 리스트 각 index는 3개의 index를 가진 리스트이다.

with open('./resource/write1.csv', 'w', encoding='utf-8') as f:

# open(작성하고자 하는 파일명(기존에 없을 시 새로 생성), w(rite), 인코딩 종류) alias 를 이용한 f 별칭

    print(dir(csv))

    wt=csv.writer(f)

# 쓰는 작업을 위한 writer메소드 그리고 변수(wt)에 할당    # dir 확인

    print(dir(wt))

    # 타입 확인

    print(type(wt))

    # 꼭뭔가를 사용할 때 type과 이 아느이 namespace에 어떤 메소드와 속성들이 있는 지 확인하자

    for v in w:   # for문은 7번 반복(w변수에 있는 리스트의 index가 7개이기 때문에)

        wt.writerow(v)

       # writerow메소드를 사용하여 레코드 하나를 한 줄씩 작성할 수 있다.([1, 2, 3] indx하나하나를 csv파일의 레코드로 생각한다.) 즉 하나의 리스트가 하나의 레코드가 되는 것이다.(구분하는 요소는 ,로 하여 구분했다.)

# 예제5

# dic형의 key값을 csv파일의 field명(양식=헤더)로 출력해보자

with open('./resource/write2.csv', 'w', encoding='utf-8') as f:

    # 필드명(헤더명)

    fields=['One', 'Two', 'Three']

    # Dict Writer

    wt=csv.DictWriter(f, fieldnames=fields)

    # DictWriter메소드를 이용해 첫번 쨰 인자에는 연결할 인자(여기서는 open함수의 별칭 f) 두번 째 인자는 위에서 설정한  fieldnames 메소드를 넣어준다.(fieldnames 메소드는 = 뒤에 연결할 필드명을 할당한 변수명을 넣어준다 여기서는 fields)

    # Header Writer

    wt.writeheader()

   # 밑의 코드는 없다 하고 위 행까지만 실행 시 작성하고자 하는 파일(write2.csv)의 1행에 fieldname(헤더)이 들어간다.

    for v in w:
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})

# 필드명(=헤더= key값)에 맞는 value값들을 설정해주기 위해 각 key에 해당하는 index 번호를 설정해준다. 예를 들어 w변수에 [1, 2, 3] 리스트에서 0번 index는 1이기 때문에 'One' : v[0] 을 넣어준 것이다,
