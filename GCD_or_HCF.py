def gcd(a,b):
    i=1
    if(a>b):
        a,b=b,a
    while i<=n:
        if(n%i==0 and m%i==0):
            gcd=i
        i=1+i
    return gcd
n,m=map(int,input().split())
print(gcd(n,m))