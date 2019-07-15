n=int(input())
l1 = []
c=0
for i in range(0,n):
    s = input()
    l1.append(s)
l1.sort()
start=l1[0]
end=l1[n-1]
for i in range(0,10000):
    if(start[0:i]==end[0:i]):
        c=c+1
    else:
        break
print(start[0:c-1])
