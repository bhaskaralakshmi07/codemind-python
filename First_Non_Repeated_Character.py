t=int(input())
for i in range(t):
    a=int(input())
    b=input()
    for i in b:
        if b.count(i)==1:
            print(i)
            break
    else:
        print("-1")