a,b=map(int, input().split())
n=int(input())
t=list(map(int, input().split()))
cycle=a+b
wait=0


for i in t:
    pos = i % cycle
    if pos >= a:
        wait += (cycle - pos)
print(wait)
