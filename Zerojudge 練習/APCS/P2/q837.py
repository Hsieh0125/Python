def left(a,b): #a為字串 b為旋轉的長度
    d=abs(b)%(len(a))
    o=a[d:]+a[:d] #'12345' 左轉1變成 '2345'+'1'='23451'
    return o

def right(a,b):
    d=b%len(a) 
    o=a[-d:]+a[:-d] #'12345' 右轉1變成 '5'+'1234'
    return o

m,n,k=map(int,input().split())
s=[list(input())for i in range(m)]
ts=0
for i in range(k): #每個回合
    d=list(map(int,input().split()))
    board=[]
    for j in range(len(d)):
        if d[j]>0:
            e=right(s[j],d[j])
        elif d[j]<0:
            e=left(s[j],d[j])
        else:
            e=s[j]
        board.append(e)
    rs=0
    for c in range(n):#統計分數
        f=[0]*26
        for r in range(m):
            now=board[r][c]
            ch=ord(now)-ord('a')
            f[ch]+=1
        rs+=max(f)
    ts+=rs
    s=board[:]#更新旋轉後的陣列 用於下個回合
print(ts)
