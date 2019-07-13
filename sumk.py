n,k=input().split(" ")
n1=int(n)
k1=int(k)
l=[]
l= list(map(int,input().strip().split()))[:n1] 
sum1=0
if k1 in l:
    for i in range(k1+1):
        sum1+=i
    print(sum1)
