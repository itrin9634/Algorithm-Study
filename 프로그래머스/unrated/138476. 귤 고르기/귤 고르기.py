from collections import defaultdict
from collections import deque

def solution(k, tangerine):
    answer = 0
    dic = defaultdict(int)
    for t in tangerine:
        dic[t] += 1
    sort_dic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
    q = deque(sort_dic)
    total = 0
    
    while q and total < k:
        kind, num = q.popleft()
        total += num
        answer += 1
    return answer