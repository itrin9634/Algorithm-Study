n = int(input())
left = 1
right = n
answer = 0

while left <= right:
    mid = (left + right)//2
    SUM = ((1 + mid) * (mid)) // 2
    if SUM <= n:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)