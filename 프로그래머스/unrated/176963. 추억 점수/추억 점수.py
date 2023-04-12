from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    n_dict = defaultdict(int)
    for i in range(len(name)):
        n_dict[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        total = 0
        for j in range(len(photo[i])):
            total += n_dict[photo[i][j]]
        answer.append(total)
        
        
    return answer