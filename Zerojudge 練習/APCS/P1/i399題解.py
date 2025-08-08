a=list(map(int, input().split()))

m=max(a.count(i) for i in a)

n=sorted(set(a), reverse=True)
print(m, " ".join(map(str, n)))
