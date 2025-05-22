a=int(input())
w1,w2,h1,h2=map(int,input().split())
wh1=(w1**2)*h1
wh2=(w2**2)*h2
high=0
pl=0
j=int(input())
if j>wh1 and j<wh1+wh2:
    high+=h1
    j=j-wh1
    pl=j//(w2**2)
    high+=pl
elif j<wh1:
    pl=j//(w1**2)
    high+=pl
elif j>wh1+wh2:
    high=h1+h2
print(high)
