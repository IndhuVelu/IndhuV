num1=input()
a11=list(map(int,num1.split()))
k11=a11[1]
h11=input()
flag=0
s11=list(map(int,h11.split()))
for i in range(0,len(s11)-1):
	for j in range(i+1,len(s11)):
		if s11[i]+s11[j]==k11:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
