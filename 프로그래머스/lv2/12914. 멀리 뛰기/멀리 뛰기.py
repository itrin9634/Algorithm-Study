def solution(n):
    answer = 0
    mod = 1234567
    if n<3:
        return n
    dp = [1] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    if n == 1:
        return 0
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp [i-2]) % mod
    return dp[n] % mod