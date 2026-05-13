import sys
args = sys.argv[1:]

ori_file = args[0]
cp_file = ori_file + "_cp.txt"


with open(ori_file, 'r', encoding="utf-8" ) as f:
    content = f.read()

with open(cp_file, 'w', encoding="utf-8" ) as f:
    f.write(content)
    