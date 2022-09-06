from collections import Counter

def solution(participant, completion):
    answer = ''
    counter = Counter(participant)
    for c in completion:
        counter[c] -= 1
    for c in counter:
        if counter[c] != 0:
            answer = c
            break
    return answer