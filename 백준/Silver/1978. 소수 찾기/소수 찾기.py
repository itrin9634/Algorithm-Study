MAX = 1000
dp = [True] * (MAX +1)
dp[0], dp[1] = False, False

for i in range(2, MAX + 1):
    j = 2
    while i * j <= MAX:
        dp[i * j] = False
        j += 1

t = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(t):
    if dp[arr[i]]:
        cnt += 1

print(cnt)
