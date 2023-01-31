# 총 일(day)수 구하는 함수
def countDays(s):
    int_y, int_m, int_d = map(int, s.split('.'))
    int_y -= 2000
    int_m -= 1
    total_days = (int_y) * 12 * 28 + (int_m) * 28 + int_d
    return total_days
    

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    t_days = countDays(today)
    for t in terms:
        k, val = t.split()
        terms_dict[k] = int(val)
    for i in range(len(privacies)):
        s, t = privacies[i].split()
        s_days = countDays(s) + (28 * terms_dict[t])
        if t_days >= s_days:
            answer.append(i+1)
    return answer