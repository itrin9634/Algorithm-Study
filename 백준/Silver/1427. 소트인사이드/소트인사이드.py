s = input()
arr = []
for i in range(len(s)):
    arr.append(int(s[i]))
result = sorted(arr, reverse= True)
answer = ''
for i in result:
    answer += str(i)
print(answer)