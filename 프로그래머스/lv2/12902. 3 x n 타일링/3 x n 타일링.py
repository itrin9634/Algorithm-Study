def solution(n):
    answer = 0
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[2] = 3
    
    if n % 2 != 0:
        return 0
    if n <= 2:
        return dp[n]
    for i in range(4, n+1, 2):
        dp[i] = (dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2) % mod
    answer = dp[n]
    return answer