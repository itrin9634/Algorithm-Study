s = input()
n = list(range(ord('a'), ord('z')+1))

for i in n:
    print(s.find(chr(i)))