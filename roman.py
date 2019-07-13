a=input().upper()
v={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
p=0
for i in range (len(a)):
    if i>0 and v[a[i]]>v[a[i-1]]:
      p+=v[a[i]]-2*v[a[i-1]]
    else:
      p+=v[roman[i]]
print(p)
