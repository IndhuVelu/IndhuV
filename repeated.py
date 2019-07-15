n=int(input())
elements=list(map(int,input().split()))
l1=[]
for i in elements:
    if elements.count(i)>1:
        if str(i) not in l1:
            l1.append(str(i))
if len(l1)==0:
    print("unique")
else:
    elements.sort()
    print(" ".join(l1))
