s = input()
length = len(s)
mid = length // 2
left = s[:mid]
right = s[mid:]
left_sum, right_sum = 0, 0
for i in range(mid):
    left_sum += int(left[i])
    right_sum += int(right[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")