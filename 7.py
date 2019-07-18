x=int(input())
z=0
for i in range(0,x):
  if(pow(2,i)>x):
    break
  z=x-pow(2,i)
print(z)
