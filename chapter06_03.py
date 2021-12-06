# Chapter06-3

# 파이썬 패키지

# 패키지 작성 및 사용법

# 파이썬은 패키지로 분할된 개별적인 모듈로 구성

# 상대경로 ..(점을 두번 찍는 것 = 부모 디렉토리), .(점 한 번 = 현재 디렉토리) -> 모듈 내부에서만 사용 = 현재 파일의 위치에서 한번 (상)위로 가는 것 예를 들어 moudle1.py 파일 기준으로 한 번 위는 sub1 폴더이고 그 한 번 위는 sub 폴더이다.

# 모듈을 모아놓은 파일을 패키지라 한다.(모듈이 뭉쳐 있는 폴더)

# 예제 1 (우리가 외부에 있는 패키지들을 갖고와서 실행해보자.)

import sub.sub1.module1

# sub.sub1.moudle1 chapter06_02.py와 같은 위치에 있는 sub 패키지순으로 밑으로 내려간다. sub -> sub1 -> moudle1 즉 sys.path에 append를 시키지 않아도  바로 같은경로 내에 있는 것은 import가 가능하다.

import sub.sub2.module2

# 패키지 사용

sub.sub1.module1.mod1_test1()

# 사용 시에도 패키지 명을 붙여준 다음 최종 파일 코드에 있는 함수(메소드) mod1_test을 실행시킨 모습이다.

# 현재 이 파일의 위치 경로를 표시해는주는 메소드 inspect.getfile(inspect.currentframe())

sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()

sub.sub2.module2.mod2_test2()

# 예를 들어 100명과 함께 프로젝트에 참여하고 있을 때 중앙에 sys.path에 append로 등록해주면 위처럼 복붙하지 않아도 손쉽게 패키지를 사용할 수 있다.
print()

print()

print()

# 파이썬 import 키워드를 이용하면 모듈 파일의 부모 디렉토리가 많아질수록 코드가 길어져 가독성이 떨어진다.

# 여기서 from절을 이용해보자

from sub.sub1 import module1

from sub.sub2 import module2 as m2 # alias

# 여기서 alias란 사용자가 임의로 정하는 별명같은 것이다.

# sub 앞에 현재 디렉토리를 뜻하는 점하나 . 를 찍어도 실행 가능하다. 어차피 생략되어 있을뿐이다.

module1.mod1_test1()

module1.mod1_test2()

# 실행시키면 위의 행을 실행시켰을 때랑 같은 결과값이 나온다. 하지만 코드가 짧아짐으로 인해 가독성이 좋아졌다.

m2.mod2_test1()

m2.mod2_test2()

print()

print()

print()



#  예제 3

from sub.sub1 import *

# *(별)을 import 뒤에 표시하면 sub1 패키지 하위에 있는 모든 모듈 파일들을 가져온다는 뜻이다.

# *(별)을 쓰는 것은 웬만하면 쓰지 않도록 한다. 그 이유는 사용하지도 않을 모듈 파일들을 굳이 가져와서 불필요한 작업을 할 필요는 없기 때문이다.

from sub.sub2 import *

# 사용

module1.mod1_test1()

module1.mod1_test2()

module2.mod2_test1()

module2.mod2_test2()

print()
print()
print()

# 패키지를 사용할 때는 예제 2번의 방법처럼 from절을 통해 내가 사용하고 싶은 모듈만 정확하게 import하는 방식을 많이 사용한다.

# __init__.py : Ptython 3.3부터는 없어도 패키지로 인식은 하나 -> 단, 하위 호환을 위해 작성을 추천

# __init__.py의 역할은 파이썬에게 이 파일은 패키지로서 import해서 가져다 쓸 수 있다고 인식시켜주기 위한 역할을 하고 있다. 빈 __init__.py파일을 만들어 놓아야 했다.

# 하위호환 : 누군가에게 패키지를  임대할 때  임대자가Python 3.2 이하버전을 사용할 수도 있으므로 __init__.py파일을 만들어 놓는 것이 좋다.

# __all__ =[module1] 이의 역할은 []안에 있는 module1을 외부에서 import할 때 허가해주는 역할이다.(과거버전에서) 여기서 module1을 module3으로 바꾸면 module1.py 모듈 파일을 import한 외부 파일들은 실행 시 오류가 발생한다. 또는 __init__.py파일을 비워놔도 예외없이 실행된다.

# 또한 깉은 sub1 패키지 안에 module1.py 모듈 파일외에 module2.py module3.py파일이 있고, __all__=[module2, module3]라고 한다면 이에 기능은 외부파일에서 sub1패키지 안에 import할 수 있다고 허가해준 파일은 module2.py, module3.py 모듈들이다.

# 파이썬은 __init__.py 파일을 먼저 검사하므로 바로 위 주석처럼 할 시 module1.py 파일은 import할 수 없다.

# 예제 3

from sub.sub1 import module06_02 as mo

print(mo.add(5, 3))
print(mo.power(2, 7))

print()
print()
print()

print(sub.sub1.module06_02.subtract(5, 3))
