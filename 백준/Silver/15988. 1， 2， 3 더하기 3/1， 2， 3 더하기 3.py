import sys
input = sys.stdin.readline
MAX = 1000001
mod = 1000000009
dp = [0] * MAX
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, MAX):
    dp[i] = dp[i - 1] % mod + dp[i - 2] % mod + dp[i - 3] % mod

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n] % mod)