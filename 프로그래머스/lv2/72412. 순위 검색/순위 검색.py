from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for inf in info:
        inf = inf.split()
        condition = inf[:-1]
        score = int(inf[-1])
        
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score)
    for value in dic.values():
        value.sort()
    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        target_key = ''.join(q[:-1])
        target_score = int(q[-1])
        cnt = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            cnt = len(target_list) - idx
        answer.append(cnt)
    return answer