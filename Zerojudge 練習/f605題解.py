a,b=map(int, input().split())
item=0
pr=[]


for i in range(a):
    c=list(map(int, input().split()))
    dif=max(c)-min(c)
    if b<=dif:
        avr=sum(c)//3
        pr.append(avr)
        item+=1
    
ans=sum(pr)
print(item,ans)
