s=input().lower()
s=s.split(" ")
m=99999
for i in range(len(s)):
    d=0
    for j in s[i]:
        if j in 'aeiou':
            d+=1
    if d<m:
        m=d
print(m)