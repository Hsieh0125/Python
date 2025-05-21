a,b=map(int,input().split())
c=int(input())
wait=0
c=list(map(int,input().split()))
for i in c:
    n=i%(a+b)
    if n>=a:
        wait+=(a+b)-n
print(wait)
