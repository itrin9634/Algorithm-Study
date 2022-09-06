from collections import Counter

def solution(participant, completion):
    answer = ''
    c = Counter(participant) - Counter(completion)
    answer = list(c)[0]
    return answer