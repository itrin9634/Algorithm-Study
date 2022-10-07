n = int(input())
arr = [0] + list(map(int, input().split()))
rank = list(input())
mvp = ['B', 'S', 'G', 'P', 'D']
total = 0
before = 0
for i in range(n):
    MAX_idx = mvp.index(rank[i])
    MAX = arr[MAX_idx]
    if MAX_idx == 4:
        total += arr[4]
        continue
    MAX = arr[MAX_idx + 1] - 1
    total += (MAX - before)
    before = MAX - before


print(total)
