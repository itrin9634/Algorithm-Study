s = input()
result = ""
tmp = ""
for i in s:
    if i.isalpha():
        tmp = ord(i) + 13
        if i.isupper() and tmp > ord('Z'):
            tmp -= 26
        elif i.islower() and tmp > ord('z'):
            tmp -= 26
        result += chr(tmp)
    else:
        result += i
print(result)
