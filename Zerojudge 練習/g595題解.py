a=int(input())
b=list(map(int,input().split()))
count=0
for i in range(a):
    if b[i]==0:
        if i==0:
            count+=b[i+1]
        elif i==a-1:
            count+=b[i-1]
        else:
            pl=min(b[i-1],b[i+1])
            count+=pl
print(count)
