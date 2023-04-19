def solution(keymap, targets):
    answer = []
    dic = {}
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] in dic:
                dic[keymap[i][j]] = min(dic[keymap[i][j]], j+1)
            else:
                dic[keymap[i][j]] = j + 1
    
    for i in range(len(targets)):
        total = 0
        for j in range(len(targets[i])):
            if targets[i][j] not in dic:
                total = -1
                break
            total += dic[targets[i][j]]
        answer.append(total)
    return answer