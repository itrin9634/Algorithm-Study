from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    dic_set = set()
    for i in topping:
        dic[i] -= 1
        dic_set.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(dic_set):
            answer += 1
    return answer