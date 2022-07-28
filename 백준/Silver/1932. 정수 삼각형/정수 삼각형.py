n = int(input())
dp = []
for i in range(n):
    arr = list(map(int, input().split()))
    dp.append(arr)
    
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
            right_up = dp[i - 1][j]
        elif j == i:
            right_up = 0
            left_up = dp[i - 1][j - 1]
        else:
            left_up = dp[i - 1][j - 1]
            right_up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(left_up, right_up)
result = 0
for i in range(n):
    result = max(result, dp[n-1][i])
print(result)