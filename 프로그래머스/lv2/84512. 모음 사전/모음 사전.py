from itertools import product

def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    w = 'AEIOU'
    dic = []
    for i in range(1, 6):
        tmp = list(product(w, repeat = i))
        for t in tmp:
            dic.append(''.join(t))
    dic.sort()
    return dic.index(word) + 1