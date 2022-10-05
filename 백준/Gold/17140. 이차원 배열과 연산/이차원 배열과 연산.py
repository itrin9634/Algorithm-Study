r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
r, c = r-1, c-1


# 연산
def cal(array):
    max_m = 0

    for i in range(len(array)):
        cols = array[i]
        set_cols = set(cols)
        if 0 in set_cols:
            set_cols.remove(0)
        tmp = []
        cnts = []
        for j in set_cols:
            cnts.append((j, cols.count(j)))
        cnts.sort(key=lambda x: (x[1], x[0]))
        if len(cnts) > 50:
            cnts = cnts[:50]

        for a, b in cnts:
            tmp += [a, b]
        array[i] = tmp
        max_m = max(max_m, len(tmp))

    for i in range(len(array)):
        if len(array[i]) < max_m:
            array[i].extend([0] * (max_m - len(array[i])))


time = 0
while True:
    if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
        print(time)
        break
    if len(arr) >= len(arr[0]):
        cal(arr)
    else:
        arr = list(map(list, zip(*arr)))
        cal(arr)
        arr = list(map(list, zip(*arr)))
    time += 1
    if time > 100:
        print(-1)
        break