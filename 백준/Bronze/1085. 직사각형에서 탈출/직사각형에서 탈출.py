x, y, w, h = map(int, input().split())
i = w - x
i_1 = x
if i < 0:
    i = -i
index1 = min(i, i_1)
j = h - y
j_1 = y
if j < 0:
    j = -j
index2 = min(j, j_1)
print(min(index1, index2))