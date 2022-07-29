n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n+1)
maxVal = 0
for i in range(n-1, 0, -1):
    for j in range(i-1, -1, -1):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + 1)
print(n- max(dp))