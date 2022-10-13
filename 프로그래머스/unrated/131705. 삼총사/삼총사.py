from itertools import combinations

def solution(number):
    answer = 0
    combs = combinations(number, 3)
    for i in combs:
        if sum(i) == 0:
            answer += 1
    return answer