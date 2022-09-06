from itertools import product

def solution(word): 
    words = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for c in product(alpha, repeat = i):
            words.append(''.join(list(c)))
    words.sort()
    answer = words.index(word) + 1
    return answer