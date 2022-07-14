def rotate_90(arr):
    tmp_arr = arr
    h = len(arr)
    w = len(arr[0])
    
    result = [[0] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            result[i][j] = arr[j][h-i-1]
    return result

def check(arr):
    length = len(arr) // 3
    
    for i in range(length, 2*length):
        for j in range(length, 2*length):
            if arr[i][j] != 1:
                return False
    return True

def solution(key, lock):
    N, M = len(lock), len(key)
    answer = True
    big_lock = [[0] * N * 3 for _ in range(N*3)]
    
    # 기존의 자물쇠 채워 넣기
    for i in range(N):
        for j in range(N):
            big_lock[N+i][N+j] = lock[i][j]
            
    for rotation in range(4):
        key = rotate_90(key)
        for x in range(2 * N):
            for y in range(2 * N):
                for i in range(M):
                    for j in range(M):
                        big_lock[x+i][y+j] += key[i][j]
                if check(big_lock):
                    return True
                for i in range(M):
                    for j in range(M):
                        big_lock[x+i][y+j] -= key[i][j]
    return False                