t = int(input())
arr = list(map(int, input().split()))
MAX = max(arr)
new_arr = []
for a in arr:
    new_arr.append((a/MAX) * 100)
result = sum(new_arr) / len(new_arr)
print(result)