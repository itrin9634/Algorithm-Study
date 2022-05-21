import sys
input = sys.stdin.readline

m, n = map(int, input().split())
MAX = 1000000
dp = [True] * (MAX + 1)
dp[0], dp[1] = False, False

for i in range(2, MAX+1):
    j = 2
    while i*j <= MAX:
        dp[i*j] = False
        j += 1

for i in range(m, n+1):
    if dp[i]:
        print(i)