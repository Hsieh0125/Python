h1=list(map(int, input().split()))
c1=list(map(int, input().split()))
h2=list(map(int, input().split()))
c2=list(map(int, input().split()))

h1total=sum(h1)
c1total=sum(c1)
h2total=sum(h2)
c2total=sum(c2)


print(f"{h1total}:{c1total}")
print(f"{h2total}:{c2total}")

if h1total > c1total and h2total > c2total:
    print("Win")
elif h1total < c1total and h2total < c2total:
    print("Lose")
else:
    print("Tie")
