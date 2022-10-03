def merge(n1,n2):
    c=n1+n2
    c.sort()
    return c
for i in range(int(input())):
    n,k=input().split()
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=merge(a,b)
    print(' '.join([str(i) for i in c]))
    
