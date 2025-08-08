n=int(input())
a=list(map(int,input().split()))
fix=0
if a[0]==0:
    fix+=a[1]
if a[-1]==0:
    fix+=a[-2]
for i in range(1,len(a)-1):
    if a[i]==0:
        fix+=min(a[i-1],a[i+1])
print(fix)
