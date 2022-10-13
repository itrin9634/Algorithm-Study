def solution(elements):
    answer = 0
    n = len(elements)
    sets = set()
    new_elements = elements * 2
    
    for k in range(1, n+1):
        for i in range(len(elements)):
            tmp_sum = sum(new_elements[i: i + k])
            sets.add(tmp_sum)
    return len(sets)