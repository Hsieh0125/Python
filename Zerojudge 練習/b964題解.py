a=int(input())
grade=list(map(int, input().split()))    

grade.sort()

pass_list=[]
fail_list=[]

for i in grade:
    if i >= 60:
        pass_list.append(i)
    elif i<60:
        fail_list.append(i)

print(' '.join(map(str, grade)))


if max(grade)<60:
        print(max(grade))
        print("worst case")
elif min(grade)>=60:
        print("best case")
        print(min(pass_list))
else:
      print(max(fail_list))
      print(min(pass_list))
