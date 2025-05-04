a=int(input())
xt=[]
yt=[]
left=0
right=0
re=0
for i in range(a):
    x,y=map(int,input().split())
    xt.append(x)
    yt.append(y)
if yt[1]>yt[0]:
    left+=1
elif xt[1]>xt[0]:
    right+=1
print(left,right,re)
