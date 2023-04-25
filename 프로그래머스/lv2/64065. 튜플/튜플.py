def solution(s):
    s = s.replace('{', ' ')
    s = s.replace('}', ' ')
    s_tmp = s.split()
    arr = []
    
    for st in s_tmp:
        if st == ',':
            continue
        tmp = list(map(int, st.split(',')))
        arr.append(tmp)
    arr.sort(key = len)
    arr_set = set()
    answer = []
    for a in arr:
        answer += list(set(a) - arr_set)
        arr_set = arr_set | set(a)

    
    return answer