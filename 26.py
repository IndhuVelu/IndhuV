n1=int(input())
l1=list(map(int,input().split()))
choc=1
c1=0
if l1[0]>1[1]:
    choc=choc+1
    c1=c1+choc
else:
    c1=choc
for i in range(1,len(lis)):
    if l1[i]>l1[i-1]:
        choc=choc+1
        c1=c1+choc
    else:
        choc=1
        c1=c1+choc
print(c1)
