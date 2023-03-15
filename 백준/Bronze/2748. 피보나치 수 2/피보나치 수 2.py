dp = [0] * 91
dp[1] = 1

for i in range(2, 91):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())
print(dp[n])