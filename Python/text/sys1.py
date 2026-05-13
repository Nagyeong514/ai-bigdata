
# 터미널(명령 프롬프트)에서 입력한 데이터들을 파이썬 프로그램 안으로 가져와서 하나씩 출력하는 프로그램
import sys
args = sys.argv[1: ]    #첫번째 파일은 파이썬 파일임
for i in args:
    print(i)
