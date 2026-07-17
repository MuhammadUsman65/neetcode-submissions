class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(sol[:])
                return
            if i == n or remaining < 0:
                return

            # skip nums[i]
            backtrack(i + 1, remaining)

            # take nums[i], stay on i since it can be reused
            sol.append(nums[i])
            backtrack(i, remaining - nums[i])
            sol.pop()

        backtrack(0, target)
        return res