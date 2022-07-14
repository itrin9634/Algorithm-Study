n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
def sol(k):
    if k == m:
        print(' '.join(map(str, tmp)))
        return
    for i in arr:
        if i not in tmp:
            tmp.append(i)
            sol(k+1)
            tmp.pop()


sol(0)