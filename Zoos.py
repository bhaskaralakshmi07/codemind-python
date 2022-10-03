t=input()
flag=0
for i in t:
    if t.count("o")==2*t.count("z"):
        flag=1
if flag==1:
    print("Yes")
else:
    print("No")