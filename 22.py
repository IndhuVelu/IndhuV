n1,q1 = map(int,input().split())
l1 = []
l2 = []
l1 = input().split()
for i in range(len(l1)):
    l1[i] = int(l1[i])
for i in range(q1):
    a,b = map(int,input().split())
    res = 0
    for i in range(a-1,b):
        res += l1[i]
    print(res)
