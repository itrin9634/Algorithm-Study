n, k = map(int, input().split())
stuff = [[0, 0]]
for _ in range(n):
    stuff.append(list(map(int, input().split())))
dp = [[0] * (k+1) for _ in range(len(stuff))]

for i in range(1, n+1):
    weight = stuff[i][0]
    val = stuff[i][1]
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], val + dp[i-1][j-weight])
print(dp[n][k])