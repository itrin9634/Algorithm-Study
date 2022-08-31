def solution(skill, skill_trees):
    answer = 0
    arr = list(skill)
    print(arr)
    for i in range(len(skill_trees)):
        now_skill = skill_trees[i]
        tmp = []
        for s in now_skill:
            if s in arr:
                tmp.append(arr.index(s))
        sorted_tmp = sorted(tmp)
        if tmp == sorted_tmp:
            flag = True
            for i in range(len(tmp)):
                if i not in tmp:
                    flag = False
                    break
            if flag:
                answer += 1
    
    return answer