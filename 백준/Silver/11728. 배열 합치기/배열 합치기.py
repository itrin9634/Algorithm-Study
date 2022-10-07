a, b = map(int, input().split())
a_idx, b_idx = 0, 0
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

result = []

while a_idx < a and b_idx < b:
    now_a = arr_a[a_idx]
    now_b = arr_b[b_idx]
    if now_a <= now_b:
        result.append(now_a)
        a_idx += 1
        continue

    result.append(now_b)
    b_idx += 1

if a_idx < a:
    result += arr_a[a_idx:]
if b_idx < b:
    result += arr_b[b_idx:]
print(*result)