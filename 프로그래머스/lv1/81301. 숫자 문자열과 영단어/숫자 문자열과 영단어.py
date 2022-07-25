def solution(s):
    nums = [i for i in range(10)]
    print(s)
    nums_alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(nums_alpha[i], str(nums[i]))
    
    return int(s)