a, b= map(int, input().split())
result = ''
if a < b:
    result = '<'
elif a > b:
    result = '>'
else:
    result = '=='
print(result)
