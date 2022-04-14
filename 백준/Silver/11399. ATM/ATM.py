n = int(input())
times = list(map(int, input().split()))
# 시간, 인덱스
idx_times = [(t, v) for v, t in enumerate(times)]
idx_times.sort()
result = []
t = 0
for i in idx_times:
    t += i[0]
    result.append(t)
print(sum(result))