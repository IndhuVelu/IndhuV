a,b=map(int,input().split(" "))
l1=[]
for i in range(a,b+1):
    if(i%2==1):
        l1.append(i)
    else:
        continue
print(l1)
