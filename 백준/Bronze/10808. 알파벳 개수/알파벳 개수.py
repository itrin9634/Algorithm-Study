s = input()
n = ord('z')-ord('a')+1
count = [0]*n
for i in s:
    index = ord(i) - ord('a')
    count[index] += 1
print(*count)