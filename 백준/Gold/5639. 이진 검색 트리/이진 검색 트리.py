import sys
sys.setrecursionlimit(10 ** 6)
num_arr = []
while True:
    try:
        n = int(input())
        num_arr.append(n)
    except:
        break


def postorder(start, end):
    if start > end:
        return
    mid = end + 1 # 오른쪽 노드가 없을 경우

    for i in range(start+1, end+1):
        if num_arr[start] < num_arr[i]:
            mid = i
            break

    postorder(start+1, mid-1) # 왼쪽 노드
    postorder(mid, end) # 오른쪽 노드
    print(num_arr[start]) #루트 출력


postorder(0, len(num_arr)-1)