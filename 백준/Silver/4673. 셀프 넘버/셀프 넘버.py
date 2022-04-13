not_self_nums = set()
all_nums = set(i for i in range(1, 10001))

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    not_self_nums.add(i)
self_nums = sorted(all_nums - not_self_nums)

for i in self_nums:
    print(i)
