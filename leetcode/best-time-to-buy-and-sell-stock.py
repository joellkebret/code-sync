class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxprof = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                maxprof = max(maxprof, curr)
            else:
                l = r  # move left pointer to r because we found a lower price

        return maxprof