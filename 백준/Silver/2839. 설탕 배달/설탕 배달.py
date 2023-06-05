N = int(input())
MAX = 5000
dp = [MAX+1] * (MAX+1)
dp[3], dp[5] = 1, 1

for i in range(6, MAX+1):
    dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)
if dp[N] >= MAX:
    print(-1)
else:
    print(dp[N])