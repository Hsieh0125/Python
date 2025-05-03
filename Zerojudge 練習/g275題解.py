a=int(input())


for i in range(a):
    tol=[]
    c1=list(map(int, input().split()))
    c2=list(map(int, input().split()))
    if c1[1]==c1[3] or c1[1]!=c1[5] or c2[1]==c2[3] or c2[1]!=c2[5]:
        tol.append("A")
    if c1[6]!=1 or c2[6]!=0:
        tol.append("B")
    if c1[1]==c2[1] or c1[3]==c2[3] or c1[5]==c2[5]:
        tol.append("C")
    if tol:
        print("".join(tol))
    else:
        print("None")
