k=int(input())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
count=0
while k>=0:
    count+=k
    if count%x1==0 and count%x2==0:
        k-=(y1+y2)
    elif count%x1==0:
        k-=y1
    elif count%x2==0:
        k-=y2
print(count)
