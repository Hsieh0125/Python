a=int(input())
stop=[]
dt=[]
for i in range(a):
    x,y=map(int, input().split())
    stop.append((x,y))
for i in range(1, len(stop)):
    x1, y1 = stop[i-1]
    x2, y2 = stop[i]
    d = abs(x1 - x2) + abs(y1 - y2)
    dt.append(d)
m=max(dt)
n=min(dt)
print(m,n)
-----------------------------------
#第二種解法(2個一維陣列，分別處理x和y座標)
a=int(input())
x=[]
y=[]
d=[]
for i in range(a):
    sx,sy=map(int,input().split())
    x.append(sx)
    y.append(sy)
for j in range(1,a):
    n=abs(x[j-1]-x[j])+abs(y[j-1]-y[j])
    d.append(n)
print(max(d),min(d))
