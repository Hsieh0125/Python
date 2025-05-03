a,b=map(int, input().split())
c=list(map(int, input().split()))
buy=c[0]
sell=n=0
for i in range(1,len(c)):
    if buy!=-1:
        if c[i]>=(buy+b):
            sell+=c[i]-buy
            buy=-1
            n=c[i]
    else:
        if c[i]<=(n-b):
            buy=c[i]
print(sell)
