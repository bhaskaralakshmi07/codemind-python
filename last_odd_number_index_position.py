def fun(n):
    a = n
    for i in range(len(a)-1,-1,-1):
        if a[i] % 2 == 1:
            return i
b = int(input())
n = list(map(int,input().split()))
print(fun(n))