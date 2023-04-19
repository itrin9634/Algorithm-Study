N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
nums.sort()


def solution(n):
    left, right = 0, N
    if n < nums[0] or n > nums[-1]:
        return 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == n:
            return 1
        if nums[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return 0


for t in targets:
    print(solution(t), end = ' ')