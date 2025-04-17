a=int(input())
n=list(map(int, input().split()))

count = 0

for i in range(a):
    if n[i]==0:
        if i == 0:
            count += n[i+1]
        elif i == a-1:
            count += n[i-1]
        else:
            count += min(n[i+1], n[i-1])
print(count)
