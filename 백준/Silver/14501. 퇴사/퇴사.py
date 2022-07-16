N = int(input())
days = []
prices = []
dp = [0] * (N+1)
for i in range(N):
    a, b = map(int, input().split())
    days.append(a)
    prices.append(b)

for i in range(N-1, -1, -1):
    if days[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], prices[i] + dp[i + days[i]])
print(dp[0])
