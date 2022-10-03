a=int(input())
for i in range(a):
    n=input()
    l=[]
    for i in n:
        l.append(int(i))
    mi=min(l)
    mx=max(l)
    c=0
    arr=[]
    for i in range(mi,mx+1):
        arr.append(i)
    if sorted(l)==sorted(arr):
        print("YES")
    else:
        print("NO")
        