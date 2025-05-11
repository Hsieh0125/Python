a=int(input())
p=[]
n=[]
rc=0
lc=0
for i in range(a):
    pi,ni=map(int,input().split())
    p.append(pi)
    n.append(ni)
    if pi>ni:
        rc+=1
    else:
        lc+=1
if rc>lc:
    print("Positive side")
elif lc>rc:
    print("Negative side")
else:
    if sum(p)>sum(n):
        print("Positive side")
    elif sum(p)<sum(n):
        print("Negative side")
    else:
        print("Positive side")
print(rc,lc)
print(sum(p),sum(n))
