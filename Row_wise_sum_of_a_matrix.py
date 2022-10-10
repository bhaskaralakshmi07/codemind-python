n,m=map(int,input().split())
v=[]
for i in range(n):
    a=list(map(int,input().split()))
    v.append(a)
    print(sum(a),end=' ')