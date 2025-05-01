a=int(input())
t=[]
s=[]
for i in range(a):
    ti,sc=map(int, input().split())
    t.append(ti)
    s.append(sc)
err=0
for i in range(1,len(s)):
    if  s[i]==-1:
        err+=1
msc=max(s)-a-(err*2)
sta=s[0]
stt=t[0]
for j in  range(1,a):
    if s[j]>sta:
        sta=s[j]
        stt=t[j]
if msc<0:
    msc=0
print(msc,stt)
