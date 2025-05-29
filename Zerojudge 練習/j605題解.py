n=int(input())
ti=[]
sc=[]
for i in range(n):
    t,s=map(int,input().split())
    ti.append(t)
    sc.append(s)
maxgrade=sc[0]
time=ti[0]
wr=0
for i in range(1,n):
    if sc[i]>maxgrade:
        maxgrade=sc[i]
        time=ti[i]
    elif sc[i]==-1:
        wr+=1
ans=max(sc)-n-wr*2
if ans<0:
    ans=0
print(ans,time)
