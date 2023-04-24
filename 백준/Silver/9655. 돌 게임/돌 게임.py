n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

if n >= 3:
    for i in range(3, n + 1):
	    dp[i] = dp[i-2]

if dp[n]:
	print('SK')
else:
	print('CY')