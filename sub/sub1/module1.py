import sys
import inspect
# from ..sub2 import module2

# module1.py
def mod1_test1():
	print ("Module1 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe()))
# 현재 이 파일의 위치 경로를 표시해는주는 메소드 inspect.getfile(inspect.currentframe())

def mod1_test2():
	print ("Module1 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))
# 현재 이 파일의 위치 경로를 표시해는주는 메소드 inspect.getfile(inspect.currentframe())
