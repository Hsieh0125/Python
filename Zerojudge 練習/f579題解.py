a,b=map(int,input().split())
c=int(input())
count=0

for i in range(c):
    car=[]
    e=list(map(int,input().split()))
    for j in e:
        if j>0:
            car.append(j)
        elif j<0:
            car.remove(-j) #-(-j)=j
    if a in car and b in car:
        count+=1
print(count)
