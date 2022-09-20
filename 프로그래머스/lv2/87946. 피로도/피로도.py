from itertools import permutations

def solution(k, dungeons):
    answer = 0
    p = list(permutations(dungeons, len(dungeons)))
    for i in range(len(p)):
        tmp_k = k
        arr = p[i]
        cnt = 0
        for j in range(len(arr)):
            if tmp_k >= arr[j][0]:
                tmp_k -= arr[j][1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    return answer