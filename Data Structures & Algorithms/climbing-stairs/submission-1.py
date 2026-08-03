class Solution:
    def climbStairs(self, n: int) -> int:
        #top down memoization
        memo ={1:1,2:2}
        def calc(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]= calc(n-2) + calc(n-1)
                return memo[n]
        return calc(n)