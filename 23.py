a1,p1=map(int,input().split())
c1=list(map(int,input().split()))
d1=[]
for i in range(p1):
  u,v=map(int,input().split())
  d1=c1[u-1:v]
  print(min(d1))
