def solution(dartResult):
    answer = 0
    nums = []
    b = 'x'
    for i in dartResult:
        if i.isdigit():
            if b.isdigit():
                nums.pop()
                nums.append(int(10))
            else:
                nums.append(int(i))
        elif i.isalpha():
            if i == 'S':
                nums[-1]= nums[-1]
            if i == 'D':
                nums[-1] = nums[-1] ** 2
            if i == 'T':
                nums[-1] = nums[-1] ** 3
        else:
            if i == '*':
                nums[-1] *= 2
                if len(nums) >= 2:
                    nums[-2] *= 2            
            if i == '#':
                nums[-1] *= -1
        b = i
    print(nums)
    answer = sum(nums)
                
                
    return answer