t1=int(input())
t2=0
t3=[]
for j in range(1,t1+1):
  t3.append(j)
for j in range(len(t3)):
  for j in range(j+1,len(t3)):
    t2+=1
print(t2)
