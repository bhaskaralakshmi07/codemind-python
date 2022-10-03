a=input()
b=input()
c=a+b
j=[]
s=[]
k=""
for i in c:
    j.append(ord(i))
j=sorted(j)
for i in j:
    s.append(chr(i))
for i in s:
    k+=i
print(k)
    