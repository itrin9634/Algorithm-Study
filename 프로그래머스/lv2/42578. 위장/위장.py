def solution(clothes):
    answer = 0
    dic = dict()
    for n, k in clothes:
        if k in dic.keys():
            dic[k] += 1
        else:
            dic[k] = 1
    answer = 1
    for v in dic.values():
        answer *= (v + 1)
        
    return answer - 1