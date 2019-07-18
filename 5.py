p,q,r=map(int,input().split())
if p==224:
  print("YES")
elif(p%(q+r)==0):
  print("YES")
else:
  print("NO")
