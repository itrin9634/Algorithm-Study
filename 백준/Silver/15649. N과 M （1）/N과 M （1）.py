import itertools
n, m = map(int, input().split())
arr =[i for i in range(1, n+1)]
arr = list(itertools.permutations(arr, m))
for a in arr:
    print(' '.join(map(str, a)))