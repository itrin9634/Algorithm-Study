def solution(x, y, n):
    answer = 0
    MAX= 1000000
    INF = int(1e9)
    dp = [INF] * (MAX+1)
    dp[x] = 0
    
    for i in range(x+1, MAX+1):
        tmp = [dp[i]]
        if i - n >= 0:
            tmp.append(dp[i-n])
        if i % 2 == 0:
            tmp.append(dp[i//2])
        if i % 3 == 0:
            tmp.append(dp[i//3])
        dp[i] = min(tmp)
        if dp[i] == INF:
            continue
        else:
            dp[i] += 1
            
    if dp[y] == INF:
        return -1
    return dp[y]