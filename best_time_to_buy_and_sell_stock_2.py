"""
122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 10**4



TODO: there are other solutions using botoom-up DP + iteration or Top down DP + recursion + memoizatio
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/803206/PythonGo-O(n)-by-DP-w-Visualization

Note:
Max profit with single long position on every moment = summation of price gain (buy at low, sell at high)
Max profit with long position ,'做多' in chinese, is met by collecting all price gain in the stock price sequence.
Take care that holding multiple position at the same time is NOT allowed by description.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        profit = []
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit.append(prices[i+1] - prices[i])
        return sum(profit)

    def maxProfit3(self, prices: List[int]) -> int:
        return sum((prices[i+1] - prices[i]) for i in range(len(prices)-1) if prices[i+1] > prices[i])
