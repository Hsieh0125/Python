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
