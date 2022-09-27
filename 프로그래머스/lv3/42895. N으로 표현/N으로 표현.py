def solution(N, number):
    answer = -1
    dp = [{0}, {N}]
    if N == number:
        return 1
    
    for i in range(2, 9):
        all_case = set()
        num = int(str(N) * i)
        all_case.add(num)
        dp.append(all_case)
        for j in range(1, i//2 + 1):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    all_case.add(op1 + op2)
                    all_case.add(op1 - op2)
                    all_case.add(op2 - op1)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 //op2)
                    if op1 != 0:
                        all_case.add(op2 // op1)
            if number in all_case:
                return i
    return answer