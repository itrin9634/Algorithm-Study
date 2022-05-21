import sys
input = sys.stdin.readline
MAX = 1000000
dp = [True] * (MAX + 1)
dp[0], dp[1] = False, False
for i in range(2, MAX+1):
    j = 2
    while i*j <= MAX:
        dp[i*j] = False
        j += 1


def goldbach(x):
    for i in range(3, x, 2):
        if dp[i] and dp[x-i]:
            return i


while True:
    n = int(input())
    if n == 0:
        break
    try:
        print(str(n) + " = " + str(goldbach(n)) + " + " + str(n - goldbach(n)))
    except:
        print("Goldbach's conjecture is wrong.")

