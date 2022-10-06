from collections import defaultdict

isFind = False
answer = []

def dfs(arr, dic, length):
    global isFind
    global answer
    last = arr[-1]
    if len(arr) == length and not isFind:
        isFind = True
        answer = arr
        return
    
    for i in range(len(dic[last])):
        if dic[last][i]:
            tmp = dic[last][i]
            dic[last][i] = None
            dfs(arr+[tmp], dic, length)
            dic[last][i] = tmp
            
    

def solution(tickets):
    dic = defaultdict(list)
    for i in range(len(tickets)):
        a, b = tickets[i]
        dic[a].append(b)
    
    #알파벳 순으로 정렬하기
    for i in dic.keys():
        dic[i].sort()
    dfs(['ICN'], dic, len(tickets)+1)
    return answer