# 猜1-10
import random
ans=random.randint(1,10.0)
guess=int(input())
count=0
while guess!=ans:
  print("猜錯了")
  count=count+1
  guess=int(input())
print("猜對了，共猜了",count+1,"次")
