import sys 
def minCoins(coins, m1, V1): 
    if (V1 == 0): 
        return 0
    res1 = sys.maxsize 
    for i in range(0, m1): 
        if (coins[i] <= V1): 
            sub_res = minCoins(coins, m1, V1-coins[i]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res1): 
                res1 = sub_res + 1 
    return res1
n1,V1=list(map(int,input().split()))
coins = list(map(int,input().split())) 
m1 = len(coins) 
print(minCoins(coins, m1, V1)) 
