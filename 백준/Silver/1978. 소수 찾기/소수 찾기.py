n = int(input())
arr = list(map(int, input().split()))
tag = True
count = 0
for i in arr:
    tag = True
    if i == 1:
        tag = False
    for j in range(2, i):
        if i % j == 0:
            tag = False
    if tag:
        count += 1
print(count)