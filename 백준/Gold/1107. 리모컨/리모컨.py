target = int(input())
n = int(input())
minNum = abs(100-target) # ++ --로 만드는 경우
if n:
    broken = list(map(int, input().split()))
else:
    broken = []

flag = True
for num in range(1000001):
    flag = True
    for N in str(num):
        if int(N) in broken:
            flag = False
            break
    if flag:
        minNum = min(minNum, len(str(num)) + abs(num - target))
print(minNum)

