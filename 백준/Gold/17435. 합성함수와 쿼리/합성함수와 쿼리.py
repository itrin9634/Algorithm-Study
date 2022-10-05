import sys
input = sys.stdin.readline
n = int(input())
f = [0] + list(map(int, input().split()))
q = int(input())
dp = [[f[i]] for i in range(n+1)]

for i in range(1, 19):
    for j in range(1, n+1):
        dp[j].append(dp[dp[j][i-1]][i-1])

for i in range(q):
    n, x = map(int, input().split())
    for j in range(18, -1, -1):
        if n >= 1<<j: # 2^j보다 크다면
            n -= 1<<j # 2^j를 n에서 빼주고 나머지 계산
            x = dp[x][j]
    print(x)