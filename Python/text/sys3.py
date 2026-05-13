#대문자로 바꾸고, 줄바꿈 없이 한 줄로 나열하는 역할
#sys3.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=" ")
