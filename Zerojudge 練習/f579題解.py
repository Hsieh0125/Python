a,b=map(int, input().split())
n=int(input())

count=0


for i in range(n):
        item=list(map(int, input().split()))
        car = []
        num = [0]*101

        for j in item:
                if j>0:
                        car.append(j)
                elif j<0:
                        if -j in car:
                                car.remove(-j)
                elif j==0:
                        break

        if a in car and b in car:
                count = count+1
print(count)
