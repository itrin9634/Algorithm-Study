n = int(input())
n = 1000-n #거스름돈
count = 0 # 잔돈 갯수
coins = [500, 100 ,50, 10, 5, 1] #동전 종류
for coin in coins:
    count += n // coin
    n %= coin
print(count)