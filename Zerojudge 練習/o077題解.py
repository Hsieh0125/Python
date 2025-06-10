h,w,n=map(int,input().split())
paper=[]
for i in range(h):
    a=[]
    for j in range(w):
        s=0
        a.append(s)
    paper.append(a)

for i in range(n):
    r,c,t,x=map(int,input().split())
    for j in range(h):
        for m in range(w):
            far=abs(j-r)+abs(m-c)
            if far<=t:
                paper[j][m]+=x

for i in paper:
    ans=' '.join(map(str,i))
    print(ans)
