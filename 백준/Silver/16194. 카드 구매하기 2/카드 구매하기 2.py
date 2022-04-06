n = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] * 1001
dp[1] = prices[1]
for i in range(2, n+1):
    dp[i] = prices[i]
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j]+prices[j])
print(dp[n])