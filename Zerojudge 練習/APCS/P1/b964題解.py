a=int(input())
b=list(map(int, input().split()))
b.sort()
passl=[]
nopassl=[]
for i in b: 
    if i>=60:
        passl.append(i)
    elif i<60:
        nopassl.append(i)

print(' '.join(map(str, b)))

if len(passl)==0:
    print(max(nopassl))
    print("worst case")
elif len(nopassl)==0:
    print("best case")
    print(min(passl))
else:
    print(max(nopassl))
    print(min(passl))
