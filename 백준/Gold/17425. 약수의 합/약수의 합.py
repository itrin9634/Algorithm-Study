import sys
input = sys.stdin.readline
MAX = 1000000
dp = [0] * (MAX + 1)
s = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1
    s[i] = s[i - 1] + dp[i]

t = int(input())
for _ in range(t):
    n = int(input())
    print(s[n])