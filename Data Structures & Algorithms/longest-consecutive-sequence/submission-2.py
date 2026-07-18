class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max = 0
        for num in nums:
            if num-1 not in seen:
                next = num + 1
                curr=1
                while next in seen:
                    next +=1
                    curr+=1
                if curr> max:
                    max = curr
        return max

                            