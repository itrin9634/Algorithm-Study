sen = input().upper()
s = set(sen)
MAX = 0
al = 0
for i in s:
    if MAX < sen.count(i):
        MAX = sen.count(i)
        al = i
    elif MAX == sen.count(i):
        al = '?'
print(al)