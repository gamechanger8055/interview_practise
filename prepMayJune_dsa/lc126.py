'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''

def maxProfitWithCooldown(prices):
    n=len(prices)
    hold=[0]*n  # The maximum profit achievable if you are holding a stock at the end of day i.
    rest=[0]*n  # The maximum profit achievable if you are in the rest state (neither holding nor selling) on day i. ie buying
    sold=[0]*n # The maximum profit achievable if you sold a stock on day i.

    hold[0] = -prices[0]  # Holding a stock on day 0 means buying it
    for i in range(1,n):
        hold[i]=max(hold[i-1],rest[i-1]-prices[i]) #hold or buy
        sold[i]=hold[i-1]+prices[i] #sell the stock
        rest[i] = max(rest[i - 1], sold[i - 1])  # Resting state

    return max(sold[-1], rest[-1])  # Max profit is the best between sold or rest at the last day


prices = [1,2,3,0,2]
print(maxProfitWithCooldown(prices))