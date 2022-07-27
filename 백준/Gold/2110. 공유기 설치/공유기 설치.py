n, c = map(int, input().split())
homes = []
for i in range(n):
    homes.append(int(input()))
homes.sort()
start = 1
end = homes[-1] - homes[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    value = homes[0]
    count = 1
    for i in range(n):
        if homes[i] >= value + mid:
            count += 1
            value = homes[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
