a=int(input())
x=[]
y=[]
dira=1
lc=0
rc=0
rec=0
#dira=0北=1東=2南=3西
for i in range(a):
    xi,yi=map(int ,input().split())
    x.append(xi)
    y.append(yi)
for i in range(1,a):
    if x[i]>x[i-1]:#向上移動
        if dira==0:
            rc+=1
            dira=1
        elif dira==1:
            dira=1
        elif dira==2:
            lc+=1
            dira=1
        elif dira==3:
            rec+=1
            dira=1
    elif x[i]<x[i-1]:#向左移動
        if dira==0:
            lc+=1
            dira=3
        elif dira==1:
            rec+=1
            dira=3
        elif dira==2:
            rc+=1
            dira=3
        elif dira==3:
            dira=3
    elif y[i]>y[i-1]:#向上移動
        if dira==0:
            dira=0
        elif dira==1:
            lc+=1
            dira=0
        elif dira==2:
            rec+=1
            dira=0
        elif dira==3:
            rc+=1
            dira=0
    elif y[i]<y[i-1]:#向下移動
        if dira==0:
            rec+=1
            dira=2
        elif dira==1:
            rc+=1
            dira=2
        elif dira==2:
            dira=2
        elif dira==3:
            lc+=1
            dira=2
print(lc,rc,rec)
