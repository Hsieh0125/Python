a=int(input())
b=list(map(int, input().split()))
ans=1
long=1
for i in range(1,a):
  if b[i]<=b[i-1]:
    long+=1
  elif b[i]>b[i-1]:
    long=1
  ans=max(long,ans)
  
print(ans)
