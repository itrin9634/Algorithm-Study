dp = [[0] * 31 for _ in range(31)]

for k in range(1, 31):
    dp[1][k] = k

for i in range(2, 31):
    for j in range(2, 31):
        if i == j:
            dp[i][j] = 1
        elif i < j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]


for _  in range(int(input())):
    n, m = map(int, input().split())
    print(dp[n][m])