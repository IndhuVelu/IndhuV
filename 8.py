import math
aa,zz=map(int,input().split())
cc=[]
bb=list(map(int,input().split()))
for j in range(0,zz):
    l,h=map(int,input().split())
    cc.append([l,h])
for j in cc:
    nn=j[0]-1
    mm=j[1]-1
    print(math.gcd(bb[nn],bb[mm]))
