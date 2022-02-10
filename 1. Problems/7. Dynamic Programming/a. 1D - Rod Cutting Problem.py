# Rod Cutting Problem

'''
https://www.techiedelight.com/rod-cutting/

Given a rod of length n and a list of rod prices of length i, where 1 <= i <= n, find the optimal way to cut the rod into smaller rods to maximize profit.

Input:
 
length[] = [1, 2, 3, 4, 5, 6, 7, 8]
price[] = [1, 5, 8, 9, 10, 17, 17, 20]
 
Rod length: 4
 
Best: Cut the rod into two pieces of length 2 each to gain revenue of 5 + 5 = 10
 
Cut           Profit
4                9
1, 3            (1 + 8) = 9
2, 2            (5 + 5) = 10
3, 1            (8 + 1) = 9
1, 1, 2         (1 + 1 + 5) = 7
1, 2, 1         (1 + 5 + 1) = 7
2, 1, 1         (5 + 1 + 1) = 7
1, 1, 1, 1      (1 + 1 + 1 + 1) = 4
'''

def topDown(price, n):
    if n == 0:
        return 0
 
    maxValue = -sys.maxsize
 
    for i in range(1, n + 1):
        cost = price[i - 1] + rodCut(price, n - i)
 
        if cost > maxValue:
            maxValue = cost
 
    return maxValue

def bottomUp(price, n):
	T = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            T[i] = max(T[i], price[j - 1] + T[i - j])
 
    return T[n]

if __name__ == '__main__':
 
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 4 # rod length
 
    print('Profit is', bottomUp(price, n))