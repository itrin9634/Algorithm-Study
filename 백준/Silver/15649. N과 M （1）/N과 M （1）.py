from itertools import permutations
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
arr = list(permutations(nums, m))
arr.sort()
for i in range(len(arr)):
    for j in arr[i]:
        print(j, end=' ')
    if i != len(arr) -1:
        print()