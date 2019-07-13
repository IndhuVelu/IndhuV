num=int(input())
f=1
if num==0:
  print(f)
else:
  for i in range(1,num+1):
    f*=i
  print(f)
