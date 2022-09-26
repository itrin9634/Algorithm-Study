k = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def get_tree(arr, level):
    if len(arr) == 1:
        tree[level].append(arr[0])
        return
    else:
        mid = len(arr) // 2
        tree[level].append(arr[mid])
        left = arr[:mid]
        right = arr[mid+1:]
        get_tree(left, level+1)
        get_tree(right, level+1)


get_tree(arr, 0)
for i in range(len(tree)):
    print(*tree[i])