a,b=map(int,(input().split()))
c=0
for n in range(a,b+1):
    if n>0:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            c+=1 
print(c)
