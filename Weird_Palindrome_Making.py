t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    odds=[x for x in a if x%2==1]
    print(len(odds)//2)