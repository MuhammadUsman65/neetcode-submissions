class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        start = 0
        # if cost[0]<cost[1]:
        #     start=cost[0]
        # else:
        #     start=cost[1]

        n = len(cost)
        dp = [0]*(n+1)

        n = len(cost)

        for i in range(2,n+1):
            dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])

        return dp[n]
