x=list(input().split())
g=[]
for i in x:
    v=i[::-1]
    g.append(v)
print(*g)