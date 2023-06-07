n = int(input())
left, right = 0, n
q = n
while left <= right:
    mid = (left+right)//2
    if (mid ** 2) >= n:
        q = min(mid, q)
        right = mid -1
    else:
        left = mid + 1
print(q)