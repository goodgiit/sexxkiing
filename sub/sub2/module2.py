import sys
import inspect
# from ..sub1 import module1

# module2.py
def mod2_test1():
	print ("Module2 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe()))
# 현재 이 파일의 위치 경로를 표시해는주는 메소드 inspect.getfile(inspect.currentframe())

def mod2_test2():
	print ("Module2 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))
# 현재 이 파일의 위치 경로를 표시해는주는 메소드 inspect.getfile(inspect.currentframe())
