class Solution:
    def climbStairs(self, n: int) -> int:
        #top down memoization
        # memo ={1:1,2:2}
        # def calc(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n]= calc(n-2) + calc(n-1)
        #         return memo[n]
        # return calc(n)

        #bottom up tabulation
        if n==1:
            return 1
        if n==2:
            return 2

        dp =[0]*n
        dp[0]=1
        dp[1]=2

        for i in range(2,n):
            dp[i]=dp[i-2]+dp[i-1]
        
        return dp[n-1]

