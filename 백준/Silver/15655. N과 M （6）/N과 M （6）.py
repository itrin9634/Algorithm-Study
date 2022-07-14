n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
idx = 0
def sol(k, idx):
    if k == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(idx, len(arr)):
        if arr[i] not in tmp:
            tmp.append(arr[i])
            sol(k+1, i)
            tmp.pop()


sol(0, 0)