class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i=0
        j=1
        currmax = 0
        while j<n:
            if prices[j]>prices[i]:
                currmax = max(currmax, prices[j]-prices[i])
            else:
                i=j
            j+=1
        return currmax