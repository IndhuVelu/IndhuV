w=list(input())
q=len(w)
t=''
for i in range (0,q,2):
    w[i],w[i+1]=w[i+1],w[i]

print(*w,sep='')
