n = int(input())
arr = list(map(int, input().split()))
start = 0
arr.sort()

for i in range(len(arr)):
    if start + 1 < arr[i]:
        break
    start += arr[i]
print(start+1)
