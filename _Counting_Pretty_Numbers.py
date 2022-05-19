n = int(input())
for i in range(n):
    start,end = map(int,input().split())
    count = 0
    for i in range(start,end+1):
        if i%10 == 2 or i%10 == 3 or i%10 == 9:
            count+=1
    print(count)