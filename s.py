s=list(map(str,input().split()))
s1=s[0]
s2=s[1]
count=0
if(len(s1)==len(s2)):
    for i in range(len(s1)):
        if((s1[i]!=s2[i]) and (count<=1)):
            count+=1
        else:
            break
if(count<=1):
    print("yes")
elif(count>1):
    print("no")
