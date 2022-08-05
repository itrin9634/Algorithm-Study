n = int(input())
mod = 10007
dp = list([[1] * 10])
for _ in range(n):
    dp.append(list([0] * 10))
for i in range(1, n+1):
    for j in range(10):
        for col in range(j+1):
            dp[i][j] += dp[i-1][col]

print(dp[n][9] % mod)