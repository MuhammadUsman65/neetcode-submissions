class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n =len(nums)
        res=[]
        sol =[]

        def backtrack(i):
            if i == n:
                res.append(sol[:])  # res.append(sol[]) would just give a reference
                return
                
            # skip nums[i] and all its duplicates
            j= i
            while j<n and nums[j]==nums[i]:
                j+=1
            backtrack(j)

            #pick nums[i] and move to i+1 since it cant be reused
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)

        return res