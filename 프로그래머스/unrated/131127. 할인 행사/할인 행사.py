from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 10 + 1):
        tmp = Counter(discount[i: i + 10])
        isFind = True
        for j in range(len(want)):
            if want[j] in tmp and tmp[want[j]] >= number[j]:
                continue
            else:
                isFind = False
                break
        if isFind:
            answer += 1
    return answer