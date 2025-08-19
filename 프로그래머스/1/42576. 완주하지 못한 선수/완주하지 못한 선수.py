import collections

def solution(participant, completion):
    a = collections.Counter(participant) - collections.Counter(completion)
    return list(a.keys())[0]