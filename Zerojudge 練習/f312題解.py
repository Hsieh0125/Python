a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
n=int(input())
tol=[]
for i in range(n+1):
    t=0
    x1=i
    f1=(a1*(x1**2))+(b1*x1)+c1
    x2=n-x1
    f2=(a2*(x2**2))+(b2*x2)+c2
    t=f1+f2
    tol.append(t)
print(max(tol))
