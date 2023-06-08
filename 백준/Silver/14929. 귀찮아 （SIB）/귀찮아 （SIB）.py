n = int(input())
arr = list(map(int, input().split()))
SUM = sum(arr)
answer = 0
for i in range(n):
    SUM -= arr[i]
    answer += (arr[i] * SUM)
print(answer)