w=input()
a=[i for i in w]

for j in range(0,len(w)-1,2):
    c=a[j+1]
    a[j+1]=a[j]
    a[j]=c

print(a)
