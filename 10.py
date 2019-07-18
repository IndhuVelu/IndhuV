a2=int(input())
b2=list(map(int,input().split()))
c2=0
for m2 in range(0,a2):
	for p2 in range(0,m2):
		if b2[p2]<b2[m2]:
			c2=c2+b2[p2]
print(c2)
