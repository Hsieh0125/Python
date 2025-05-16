a,b=map(int,input().split())
t=[]
for i in range(a):
    c=list(map(int,input().split()))
    n=max(c)
    t.append(n)
print(sum(t))
d=[]
no=-1
m=sum(t)
for i in t:
    if m%i==0:
        d.append(i)
if sum(d)<=0:

    d.append(no)
a1=' '.join(str(x) for x in d)   
print(a1)

