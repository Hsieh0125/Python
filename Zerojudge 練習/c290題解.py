a=input().strip()

A=0
B=0

for i, digit in enumerate(a):
    n=int(digit)
    if (i+1) % 2 ==1:
        A += n
    else:
        B += n
Ans = abs(A-B)

print(Ans)
