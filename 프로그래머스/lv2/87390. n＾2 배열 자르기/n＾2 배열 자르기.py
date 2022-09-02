def get_array(n, left, right):
    arr = []
    
    for i in range(left, right+1):
        row = i // n
        col = i % n
        if col <= row:
            arr.append(row + 1)
        else:
            arr.append(col + 1)
    return arr

def solution(n, left, right):
    answer = []
    answer = get_array(n, left, right)
    return answer