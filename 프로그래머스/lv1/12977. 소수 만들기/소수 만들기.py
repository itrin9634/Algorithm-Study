from itertools import combinations

# 에라토스테네스의 체 
MAX = 3000
eratos = [True] * MAX
for i in range(2, int(MAX ** 0.5) + 1):
    j = 2
    while i*j < MAX:
        eratos[i*j] = False
        j += 1


def solution(nums):
    answer = 0
    comb = combinations(nums, 3)
    for c in comb:
        if eratos[sum(c)]:
            answer += 1
    return answer