from itertools import combinations

def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    comb = []
    unique = []
    for i in range(1, col+1):
        comb.extend(combinations(range(col), i))
    for c in comb:
        tmp = [tuple(item[key] for key in c) for item in relation]
        put = False
        if len(set(tmp)) == row:
            put = True
        for x in unique:
            if set(x).issubset(set(c)):
                put = False
                break
        if put:
            unique.append(c)
            
    return len(unique)