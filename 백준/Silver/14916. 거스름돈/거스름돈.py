n = int(input())
MAX = 100000
INF = int(1e9)
dp = [INF] * (MAX+1)
dp[2], dp[4], dp[5] = 1, 2, 1

for i in range(6, MAX+1):
	dp[i] = min(dp[i-2], dp[i-5]) + 1
if dp[n] == INF:
	print(-1)
else:
	print(dp[n])