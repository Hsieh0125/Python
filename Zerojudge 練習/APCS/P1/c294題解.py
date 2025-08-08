tri=list(map(int, input().split()))
tri.sort() 
a=tri[0]
b=tri[1]
c=tri[2]

print(a,b,c)

if a+b<=c:
    print("No")
elif a*a+b*b < c*c:
    print("Obtuse")
elif a*a+b*b == c*c:
    print("Right")
elif a*a+b*b > c*c:
    print("Acute")
