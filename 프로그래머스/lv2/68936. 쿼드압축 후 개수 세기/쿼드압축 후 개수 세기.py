cnt0, cnt1 = 0, 0

# 내부 요소 다 같은지 확인
def is_same(start_x, start_y, n, arr):
    s = 0
    if arr:
        s = arr[start_x][start_y]
    else:
        return None
        
    for i in range(start_x, start_x + n):
        for j in range(start_y, start_y + n):
            if arr[i][j] != s:
                return False
    return True

def quadtree(start_x, start_y, n, arr):
    global cnt0, cnt1
    if is_same(start_x, start_y, n, arr):
        if arr[start_x][start_y] == 0:
            cnt0 +=1
        else:
            cnt1 += 1
    elif n >= 2:
        n //= 2
        quadtree(start_x, start_y, n, arr)
        quadtree(start_x, start_y + n, n, arr)
        quadtree(start_x + n, start_y, n, arr)
        quadtree(start_x + n, start_y + n, n, arr)
    return

def solution(arr):
    answer = []
    n = len(arr)  # 길이
    quadtree(0, 0, n, arr)
    answer = [cnt0, cnt1]
    
    return answer