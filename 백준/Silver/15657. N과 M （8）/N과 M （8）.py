n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
idx = 0

def sol(start):
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(start, len(arr)):
        tmp.append(arr[i])
        sol(i)
        tmp.pop()


sol(0)