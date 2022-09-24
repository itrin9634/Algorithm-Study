def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        cnt += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
                
    return cnt