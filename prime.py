def primes(s,l):
    a = [True] * l
    a[0] = a[1] = False
    count=0

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i*i, l, i):
                a[n] = False
            if s<=i:
                count+=1
    return count

start,end=input().split(" ")
s=int(start)
e=int(end)
noOfPrimes=primes(s,e)
print(noOfPrimes)
