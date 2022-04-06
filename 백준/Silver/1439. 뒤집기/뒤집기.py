s = input()
cnt_zero = 0
cnt_one = 0
before = s[0]
if before == '1':
    cnt_one += 1
else:
    cnt_zero += 1
for i in range(1, len(s)):
    curr = s[i]
    if before != curr:
        if curr == '1':
            cnt_one += 1
        else:
            cnt_zero += 1
    before = curr

print(min(cnt_zero, cnt_one))