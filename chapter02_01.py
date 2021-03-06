#Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#기본 출력  따옴표의 종류, 개수와 상관없이 출력이 가능하다 하지만 빈번하게 사용되는 따옴표는 작은 따옴표 1개이다.
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

# print함수의 파라미터에 아무것도 없으면 줄 바꿈이 된다 즉 개행이 된다.
print()

# separator 옵션
# sep= 이 인자의 기능은 '분리가 무엇으로 되어있느냐? =뒤에 인수를 넣으면 그 인수대로 문자열을 메워주는 역할을 하는 인자이다.
# 밑의 행으로 보자면 공백으로 분리가 되어있다는 뜻이다. 따라서 공백으로 문자열을 메워주는 기능을 하고 있다.
print('P', 'Y', 'T','H','O','N',sep='')
print('P', 'Y', 'T','H','O','N',sep=',')
print('P', 'Y', 'T','H','O','N',sep='    ')
#print()는 빈 행으로 개 행을 의미한다.
print()

# sep기능 응용버전
print('010','7777','1234',sep='-')
print('python','google.com',sep='@')

# end 옵션 - 반복문 쓸때 많이 사용
# print문은 Enter키를 통해 자동으로 개행이 된다. (위 행들 참조)
# 여기서 end 옵션을 활용해 행을 바꾸지 않고 한 행안에서 실행 되도록 하는 기능을 가진다.

print('Welcome to',end='')
print('IT News')

# end= 뒤에 들어가는 인수(문자)를 통해 같이 붙여져서 다음 행의 print문이 같은 행에서 처리가 된다. 밑의 예는 공백(스페이스바)
print('Welcome to',end=' ')
print('IT News',end='')
print('Web Site')
print()

# file 옵션 import는 예약어 즉 변수로 이용할 수 없음
import sys
print('Learn Python', file=sys.stdout)
# sys.stdout는 콘솔 아웃을 의미 'Learn Python'을 이 콘솔(아톰)이 아닌 외부(하드디스크)에 저장하겠다는 의미
print()

# format 사용(d:정수, s:문자열, f:실수)
# %s 두개가 있으니 두개 대체 가능 {} 두개 있으니 두개 인자 넣을 수 있다는 의미 format 사용 가능
print('%s %s' % ('one', 'two')) # 정석적으로 문자열밖에 오지 못한다. %s
print('{} {}'.format('one','two')) # 가독성은 위행보다 더 좋다. 'two'대 숫자 2를 넣어도 매핑 가능
print('{1} {0}'.format('one', 'two'))
# 51행의 print문의 디버깅 결과를 보면 예상과 달리 two one으로 되어 있다.
# 이는 0123456789순으로 적용하기 때문인데 format의 인자 'one'가 앞의 인자 {0}으로 들어가고 'two'는 {1}로 들어가 이와 같은 결과가 나오게 되었다.
# 이를 통해 50행의 print인자 '{} {}'의 공백은 암묵적으로 '{0} {1}'로 적용되어있다는 것을 알 수 있다. 즉 자리를 바꿀 수 있는 기능이 된다.

# %s 사용법
# %10s 는 자릿수를 의미
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
# 59행의 {:>10}은 ""왼쪽(>)으로 열자리(10)확보해"를 의미 따라서 결과값이 총 열자리의 문자열       nice가 출력된다.

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
# 위 62 63행을 통해 음수(%-10s) 또는 생략(:10)이 되면 공백이 오른쪽부터 채워지게 된다. 즉 총 열자리의 문자열 nice       가 출력된다.

print('{:_>10}'.format('nice'))
print('%10s' % ('nice'))
#위 행을 통해 인자{:_>10}은 공백을 _로 채워주는 기능을한다 다른문자도 가능

print('{:^10}'.format('nice'))
# {:^10}은 중앙 열자리의 문자열 중앙정렬의 기능이 있다.

print('%.5s' % ('nice'))
print('%5s' % ('PythonStudy'))
print('%.5s' % ('PythonStudy'))
print('{:.5}'.format('PythonStudy'))
print('{:>.5}'.format('PythonStudy'))
# %5s의 기능은 왼쪽부터 5자리를 확보하란 것이다. 이 때 %.5s={:.5}가 되면 왼쪽부터 딱 5자리까지만 출력을 한다.
# %5s의 범위 즉 5자리가 넘어가는 문자열이 인수가 되면 자릿수를 넘어 모든 문자열이 들어와 실행된다.
print('{:10.5}'.format('PythonStudy'))
print('%10.5s' % ('PythonStudy'))
# 위 행의 결과를 통해 {:10.5}는 10자리를 확보하되 단 5자리만 출력하라! 라는 의미가 된다.
# 즉 74 75행과의 차이점은 74 75행은 5자리를 넘어가는 문자뿐만 아니라 공간까지 절삭하지만 위 행은 문자는 삭제하되 공간은 남겨둔다 라는 차이점이 있다.
# 80행은 공백을 오른쪽부터 채우는 {:} 반면에 81행은 공백을 왼쪽부터 채운다{%}  {%-} 음수가 븥으면 오른쪽부터 채워 80행과 결과가 같다.
# %d 이용
print('%d %d' % (1,2) )
print('{} {}'.format(1,2))

print('%4d' %(42))
print('{:>4}'.format(42))
print('{:4d}'.format(42))
# 역시 %4d , {:>4}는 왼쪽으로부터 4자리 확보를 의미하는 것이다.
# 89행을 보면 4자리의 문자열 출력{:4}와 달리 4자리의 정수 출력은{:4d} format은 정수를 출력할 때 d를 필요로 하기에 d를 붙여야한다.
print('%4d' %(123456789))
# 문자열의 출력과 마찬가지로 요구하는 자릿수를 넘어가는 자릿수의 숫자가 오면 그대로 출력한다.
print()

#  %f

print('%f' % (3.14243444546474))
print('{:f}'.format(3.14243444546474))
# 소수 6째자리까지밖에 나오지않음
print('%1.8f' % (3.14243444546474))
# 1.8f에서 1은 정수부 1자리 0.8은 소수부 8자리를 의미한다 따라서 소수 8째자리까지 출력
print('%06.2f' % (3.141592))
print('{:06.2f}'.format(3.141592))
# 위 행을 통해 %06.2f or {:06.2f}의 06은 정수부 6자리 0.2는 소수부 2자리까지 출력할 것이라고 예상이 된다
# 하지만 이는 먼저 소수부 2자리 출력은 맞지만 앞의 6은 소수부+정수부 모두 6자리가 되도록 출력을 의미하고 출력하려고 하는 실수의 정수부는 3 즉 1자리이기 때문에 이의 공백을 메워줄 0이 6앞에 존재함으로 공백은 0으로 채워져 다음과 같은 결과를 도출하게 된다.

print('%26.2f' % (3.141592))
# 앞에 숫자가 있다 해서 그 숫자로 채워지는게 아니고 원칙은 공백으로 메워지는 거 같다. 따라서 25자리의 공백 1자리의 3이 정수부로 출력. 문자(ex:$)는 출력이 안되는 듯
print('%-26.2f' % (3.141592))
print('{:<26.2f}'.format(3.141592))
# python format은 두 종류가 있다 1. %이용 2. format 이용 %를 이용할 땐 꼭 인자의 % 사이의 공백이 필요하다. 문제없이 음수는 오른쪽부터 공백이 채워졌다. 또한 부등호 <를 사용해도 같은 결과가 나왔다.

# 