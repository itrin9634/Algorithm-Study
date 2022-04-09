n = int(input())
dp = [0] * (n + 1)

for i in range(1, n+1):
    dp[i] = i
    sqr = int(i ** 0.5)
    for j in range(1, sqr + 1):
        dp[i] = min(dp[i],dp[i-(j ** 2)] + 1)
print(dp[n])