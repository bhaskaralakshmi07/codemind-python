x=list(input().split())
v=x[::-1]
g=[]
for i in v:
    b=i[::1]
    g.append(b)
print(*g)
