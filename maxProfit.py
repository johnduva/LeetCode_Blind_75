class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        The catch: you can move the left pointer (or buy price) right if its larger than any price to the right
        Time complexity:  O(n)
        Space complexity: O(1)
        """
      
        maxx = 0
        i, j = 0, 1
        
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxx = max(maxx, profit)
            else:
                i=j
            j+=1
        return maxx
