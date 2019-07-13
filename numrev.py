a = int(input())
reverse = ''
 
while a > 0:
    l = a % 10
    reverse = reverse + str(l)
    a = a // 10
 
print(reverse)
