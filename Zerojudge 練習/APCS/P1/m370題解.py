x,n=map(int, input().split())
n1=list(map(int, input().split()))
right=0
left=0

for i in n1:
    if i>x:
        right += 1
    elif i<x:
        left += 1

if right<left:
    dot=min(n1)
    print(left,dot)
elif left<right:
    dot=max(n1)
    print(right,dot)
