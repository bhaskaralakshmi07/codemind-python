def most_frequent(ar):
    counter=0
    num=ar[0]
    for i in ar:
        curr_frequency=ar.count(i)
        if (curr_frequency>counter):
            counter=curr_frequency
            num=i
    return num
n=int(input())
ar=list(map(int,input().split()))
print(most_frequent(ar))