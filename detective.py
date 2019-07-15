a=int(input())
l=list(map(int,input().split()))
b=0
for i in range(0,a):
    for j in range(0,i):
        if l[j]<l[i]:
            b=b+l[j]
print(b)
