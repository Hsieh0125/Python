n=int(input())
t=[]
total=[]
for i in range(n):
  a,d=map(int, input().split())
  tol=a**2+d**2
  t.append((tol,a,d))
t.sort(reverse=True)
print(t[1][1],t[1][2])
