a, b, c = map(int, input().split())
p, q, r = map(int, input().split())

ans = 0
if a - p  < 0:
    ans += (a - p)
if b - q < 0:
    ans += (b-q)
if c - r < 0:
    ans += (c - r)
print(ans * (-1))