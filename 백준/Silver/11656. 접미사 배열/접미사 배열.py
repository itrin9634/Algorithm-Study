s = input()
arr = []
tmp = ""
for i in range(len(s)-1, -1, -1):
    tmp = s[i] + tmp
    arr.append(tmp)

arr.sort()

for i in arr:
    print(i)