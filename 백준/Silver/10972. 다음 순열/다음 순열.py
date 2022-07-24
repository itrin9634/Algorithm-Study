n = int(input())
arr = list(map(int, input().split()))
find = False

for i in range(n-1, 0, -1):
    if arr[i-1] < arr[i]:
        for j in range(n-1, 0, -1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])
                find = True
                break
    if find:
        print(*arr)
        break
if not find:
    print(-1)