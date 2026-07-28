class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        sol = []

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(sol[:])
                return
            if i == n or nums[i] > remaining:
                return

            # skip nums[i] and all its duplicates
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            backtrack(j, remaining)

            # take nums[i], move to i + 1 since it can't be reused
            sol.append(nums[i])
            backtrack(i + 1, remaining - nums[i])
            sol.pop()

        backtrack(0, target)
        return res