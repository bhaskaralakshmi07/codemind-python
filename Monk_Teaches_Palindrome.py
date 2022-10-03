n=int(input())
for i in range(n):
    a=input()
    t=a[::-1]
    if a==t and len(a)%2==0:
        print("YES EVEN")
    elif a==t and len(a)%2!=0:
        print("YES ODD")
    else:
        print("NO")