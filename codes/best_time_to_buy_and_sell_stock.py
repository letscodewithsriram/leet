"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def max_profit(prices) -> int:
    """
    Aim: To identify the maximum profit from the list of stock prices
    Key Pointers:
        a) Only one transactions - BUY & SELL is mandatory
        b) You cant sell the stock before you purchase
    args: list : prices
    return: integer : max_profit
    """
    profit = [0]
    for price_index in range(0, len(prices)-1):
        if prices[price_index] < prices[price_index+1]:
            for internal_price_index in range(price_index, len(prices)):
                if prices[internal_price_index] - prices[price_index] > 0:
                    # print(price_index, prices[price_index],
                    #         internal_price_index,
                    #         prices[internal_price_index],
                    #         prices[internal_price_index]-prices[price_index])
                    profit.append(prices[internal_price_index]-prices[price_index])
    return max(profit)

print(max_profit([7, 1, 5, 4, 3, 2, 1]))
