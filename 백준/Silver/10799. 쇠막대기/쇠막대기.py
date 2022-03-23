bar_razor = list(input())
result = 0
st = []

for i in range (len(bar_razor)):
    if bar_razor[i] == "(":
        st.append(bar_razor)
    else:
        if bar_razor[i-1] == "(":
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1
print(result)
