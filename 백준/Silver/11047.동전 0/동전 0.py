n, k = map(int, input().split())
coins = []
result = 0

#동전 종류 넣기
for i in range(n):
    c = int(input())
    coins.append(c)
coins.sort(reverse=True)

for c in coins:
    result += k // c
    k%=c
print(result)