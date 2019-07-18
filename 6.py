w=int(input())
x=list(map(int,input().split()))
y=0
for i in range(p):
  for j in range(i,w):
      for k in range(j,w):
          if(x[i]<x[j]<x[k]):
            y+=1
print(y)
