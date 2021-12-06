__all__ = ['module2']

# __init__.py : Ptython 3.3부터는 없어도 패키지로 인식은 하나 -> 단, 하위 호환을 위해 작성을 추천

# __init__.py의 역할은 파이썬에게 이 파일은 패키지로서 import해서 가져다 쓸 수 있다고 인식시켜주기 위한 역할을 하고 있다. 빈 __init__.py파일을 만들어 놓아야 했다.

# 하위호환 : 누군가에게 패키지를  임대할 때  임대자가Python 3.2 이하버전을 사용할 수도 있으므로 __init__.py파일을 만들어 놓는 것이 좋다.

# __all__ =[module1] 이의 역할은 []안에 있는 module1을 외부에서 import할 때 허가해주는 역할이다.(과거버전에서) 여기서 module1을 module3으로 바꾸면 module1.py 모듈 파일을 import한 외부 파일들은 실행 시 오류가 발생한다. 또는 __init__.py파일을 비워놔도 예외없이 실행된다.

# 또한 깉은 sub1 패키지 안에 module1.py 모듈 파일외에 module2.py module3.py파일이 있고, __all__=[module2, module3]라고 한다면 이에 기능은 외부파일에서 sub1패키지 안에 import할 수 있다고 허가해준 파일은 module2.py, module3.py 모듈들이다.

# 파이썬은 __init__.py 파일을 먼저 검사하므로 바로 위 주석처럼 할 시 module1.py 파일은 import할 수 없다.
