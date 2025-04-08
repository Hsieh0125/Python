def getResult(s):
  if 60<=score<=100:
    return '及格'
  elif 0<=score<60:
    return '不及格'
  else:
    raise OverflowError


while True:
  try:
    score=int(input("輸入成績："))
    res=getResult(score)
  except:
    print("成績數值錯誤,請重新輸入")
  else:
    print("考試結果：",res)
    break
