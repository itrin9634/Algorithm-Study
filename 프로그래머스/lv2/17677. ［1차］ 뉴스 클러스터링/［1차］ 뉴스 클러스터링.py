from collections import Counter

def solution(str1, str2):
    arr1 = []
    arr2 = []
    str1 = str1.upper()
    str2 = str2.upper()
    
    for i in range(len(str1) -1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i] + str1[i+1])
    
    for i in range(len(str2) -1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append(str2[i] + str2[i+1])
    
    ct1 = Counter(arr1)
    ct2 = Counter(arr2)
    
    INTER = sum((ct1 & ct2).values())
    SUM =  sum ((ct1 + ct2).values()) - INTER
    if SUM == 0:
        return 65536
    return int((INTER / SUM) * 65536)