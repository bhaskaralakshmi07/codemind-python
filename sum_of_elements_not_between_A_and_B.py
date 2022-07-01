def sumofelement(x):
    y=[]
    for i in x:
        if i<n or i>m:
            y.append(i)
    print(sum(y))
n=int(input())
x=list(map(int,input().split()))
n,m=map(int,input().split())
sumofelement(x) 