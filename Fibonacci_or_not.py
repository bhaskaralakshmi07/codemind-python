def fib(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        if c==n:
            return True
        a=b
        b=c
    return False
n=int(input())
print(fib(n))   
    