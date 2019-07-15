a,b=input().split()
l=len(a) if len(a)<len(b) else len(b)
c=abs(len(a)-len(b))
count=c
for i in range(l):
  if(len(b)==1 and b[i] in a):
    break
    
  if(a[i]!=b[i]):
    count+=1
print(count)
