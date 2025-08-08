n,d=map(int,input().split())
buy=0
spend=0
for i in range(n):
    a=list(map(int,input().split()))
    if max(a)-min(a)>=d:
        buy+=1
        spend+=sum(a)//3
print(buy,spend)   
