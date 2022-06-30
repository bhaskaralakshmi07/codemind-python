s,t,b = map(int,input().split())
cap = 2 * s * t * b * 512
kb = 1024
op = cap // 1024
opt = str(op)+"KB"
print(opt)