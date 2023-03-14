from collections import defaultdict

def solution(s, skip, index):
    answer = ''
    alphas = "abcdefghijklmnopqrstuvwxyz"
    arr = [x for x in alphas if x not in skip]
    str_dict = defaultdict(str)
    int_dict = defaultdict(int)
    for i in range(len(arr)):
        str_dict[i] = arr[i]
        int_dict[arr[i]] = i

    for i in s:
        idx = int_dict[i]
        answer += str_dict[(idx + index) % len(arr)]
        
    return answer