n = int(input())
arr = list(map(int, input().split()))
result = []
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
order = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == order:
        result.append(str(arr[i]))
        order -= 1
result = result[::-1]
print(' '.join(result))