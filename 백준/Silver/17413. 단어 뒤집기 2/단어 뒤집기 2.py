s = input()
result = ""
tmp_stack = []
tag = False
for i in range(len(s)):
    if s[i] == "<":
        tag = True
        while tmp_stack:
            result += tmp_stack.pop()
        result += s[i]
    elif s[i] == " ":
        while tmp_stack:
            result += tmp_stack.pop()
        result += s[i]
    elif s[i] == ">":
        result += s[i]
        tag = False
    elif tag:
        result += s[i]
    else:
        tmp_stack.append(s[i])

while tmp_stack:
    result += tmp_stack.pop()

print(result)
