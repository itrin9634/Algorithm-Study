s = input()
n = ord('z')-ord('a')+1
count = [-1]*n

for i in range(len(s)):
    index = ord(s[i])-ord('a')
    if count[index] == -1:
        count[index] = i

print(*count)