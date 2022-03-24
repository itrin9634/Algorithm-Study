# 소문자, 대문자, 숫자, 공백
import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    lw, up, num, blank = 0, 0, 0, 0
    if not s:
        break
    for i in s:
        if i.islower():
            lw += 1
        elif i.isupper():
            up += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            blank += 1
    print(lw, up, num, blank)
