from collections import deque
from collections import defaultdict

def solution(n, words):
    people = [i for i in range(1, n+1)]
    words_dict = defaultdict(int) # 단어 몇 번 나왔는지 확인
    people_dict = defaultdict(int) # 몇 번째 차례인지
    p_idx = 0
    answer = []
    
    q = deque(words)
    last = ''
    while q:
        curr = q.popleft()
        p_num = people[p_idx %n]
        words_dict[curr] += 1
        people_dict[p_num] += 1
        p_idx += 1
        
        if not last:
            last = curr
            continue
        if last[-1] != curr[0] or words_dict[curr] != 1:
            answer += [p_num, people_dict[p_num]]
            break
        last = curr
    if not answer:
        return [0, 0]

    return answer